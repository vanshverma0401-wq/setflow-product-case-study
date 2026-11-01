"""Checks for the public case-study package, not the private iOS application.

The manifest binds reviewed files and asset bytes. These checks cannot establish
visual quality, privacy of pixels, app correctness, or release readiness.
"""
from __future__ import annotations

import hashlib
import json
import re
import struct
import unittest
import xml.etree.ElementTree as ET
import zlib
from datetime import date
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MAX_FILE_BYTES = 5 * 1024 * 1024
IGNORED_PARTS = {".git", "__pycache__", ".pytest_cache"}
TEXT_SUFFIXES = {".md", ".json", ".py", ".yml", ".yaml", ".svg"}


def public_paths() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*")
        if not IGNORED_PARTS.intersection(p.relative_to(ROOT).parts)
    )


def public_files() -> list[Path]:
    return [p for p in public_paths() if p.is_file()]


def manifest() -> dict:
    return json.loads((ROOT / "public-package.json").read_text(encoding="utf-8"))


def iso_date(value: object) -> date:
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ValueError("Expected an ISO date in YYYY-MM-DD form")
    return date.fromisoformat(value)


def safe_relative_path(value: object) -> str:
    if not isinstance(value, str):
        raise ValueError("Expected a relative path string")
    p = PurePosixPath(value)
    if (not value or p.is_absolute() or ".." in p.parts or "\\" in value
            or str(p) != value or IGNORED_PARTS.intersection(p.parts)):
        raise ValueError("Invalid public-package path")
    return value


def markdown_anchors(text: str) -> set[str]:
    anchors = set(re.findall(r'<a\s+(?:[^>]*\s)?(?:id|name)=["\']([^"\']+)', text))
    seen: dict[str, int] = {}
    for heading in re.findall(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$", text, re.MULTILINE):
        label = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", heading)
        label = re.sub(r"<[^>]*>", "", label).strip().lower()
        slug = re.sub(r"[^\w\- ]", "", label).replace(" ", "-")
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        anchors.add(slug if count == 0 else f"{slug}-{count}")
    return anchors


def validate_png(path: Path) -> tuple[int, int]:
    """Validate chunks, CRCs, and all decompressed scanlines, including Adam7."""
    raw = path.read_bytes()
    if raw[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("Invalid PNG signature")
    offset = 8
    chunks: list[tuple[bytes, bytes]] = []
    while offset < len(raw):
        if len(raw) - offset < 12:
            raise ValueError("Truncated PNG chunk")
        length = struct.unpack_from(">I", raw, offset)[0]
        kind = raw[offset + 4:offset + 8]
        end = offset + 12 + length
        if end > len(raw):
            raise ValueError("Truncated PNG payload")
        payload = raw[offset + 8:offset + 8 + length]
        crc = struct.unpack_from(">I", raw, offset + 8 + length)[0]
        if zlib.crc32(kind + payload) & 0xFFFFFFFF != crc:
            raise ValueError("PNG CRC mismatch")
        chunks.append((kind, payload))
        offset = end
        if kind == b"IEND":
            break
    if (not chunks or chunks[0][0] != b"IHDR"
            or sum(k == b"IHDR" for k, _ in chunks) != 1
            or chunks[-1] != (b"IEND", b"") or offset != len(raw)
            or len(chunks[0][1]) != 13):
        raise ValueError("Invalid PNG chunk structure")
    width, height, depth, color, compression, filtering, interlace = struct.unpack(
        ">IIBBBBB", chunks[0][1]
    )
    depths = {0: {1, 2, 4, 8, 16}, 2: {8, 16}, 3: {1, 2, 4, 8}, 4: {8, 16}, 6: {8, 16}}
    channels = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}
    if not width or not height or not 0 < width * height <= 16_000_000:
        raise ValueError("Invalid or excessive PNG dimensions")
    if color not in depths or depth not in depths[color]:
        raise ValueError("Invalid PNG color/depth combination")
    if compression != 0 or filtering != 0 or interlace not in {0, 1}:
        raise ValueError("Invalid PNG encoding")
    if color == 3 and not any(k == b"PLTE" for k, _ in chunks):
        raise ValueError("Indexed PNG has no palette")
    passes = [(0, 0, 1, 1)] if interlace == 0 else [
        (0, 0, 8, 8), (4, 0, 8, 8), (0, 4, 4, 8), (2, 0, 4, 4),
        (0, 2, 2, 4), (1, 0, 2, 2), (0, 1, 1, 2),
    ]
    scanlines = []
    for x, y, dx, dy in passes:
        pw = max(0, (width - x + dx - 1) // dx)
        ph = max(0, (height - y + dy - 1) // dy)
        if pw and ph:
            scanlines.append(((pw * channels[color] * depth + 7) // 8, ph))
    expected = sum((size + 1) * count for size, count in scanlines)
    compressed = b"".join(payload for kind, payload in chunks if kind == b"IDAT")
    if not compressed:
        raise ValueError("PNG has no image stream")
    decoder = zlib.decompressobj()
    decoded = decoder.decompress(compressed, expected + 1)
    if (len(decoded) != expected or not decoder.eof
            or decoder.unused_data or decoder.unconsumed_tail):
        raise ValueError("PNG scanline length/stream mismatch")
    cursor = 0
    for size, count in scanlines:
        for _ in range(count):
            if decoded[cursor] > 4:
                raise ValueError("Invalid PNG scanline filter")
            cursor += size + 1
    return width, height


class CaseStudySafetyTests(unittest.TestCase):
    def test_manifest_exactly_matches_public_files(self) -> None:
        data = manifest()
        self.assertEqual(data["schema_version"], 1)
        self.assertEqual(data["verification_scope"], "public_package_only")
        expected = [safe_relative_path(p) for p in data["files"]]
        self.assertEqual(len(expected), len(set(expected)), "Duplicate manifest path")
        actual = {str(p.relative_to(ROOT)) for p in public_files()}
        self.assertEqual(set(expected), actual, "Manifest and actual public files differ")
        self.assertIn("public-package.json", expected)
        self.assertFalse([str(p.relative_to(ROOT)) for p in public_paths() if p.is_symlink()])
        self.assertTrue(all(p.stat().st_size < MAX_FILE_BYTES for p in public_files()))

    def test_package_contains_only_reviewable_documentation_assets(self) -> None:
        forbidden = {
            ".swift", ".xcodeproj", ".xcworkspace", ".xcassets", ".plist", ".entitlements",
            ".app", ".ipa", ".dsym", ".xcresult", ".sqlite", ".sqlite3", ".store",
            ".usdz", ".usd", ".obj", ".fbx", ".pem", ".key", ".xcconfig",
        }
        findings = []
        for p in public_paths():
            relative = p.relative_to(ROOT)
            if any(PurePosixPath(part).suffix.lower() in forbidden for part in relative.parts):
                findings.append(str(relative))
            if p.is_file() and p.name != ".gitignore" and p.suffix.lower() not in TEXT_SUFFIXES | {".png"}:
                findings.append(str(relative))
        self.assertFalse(findings, findings)

    def test_no_private_locations_repository_links_or_secret_patterns(self) -> None:
        patterns = {
            "private_path": re.compile(r"/(?:Users|Volumes|home)/[^\s\x60]+"),
            "private_revision": re.compile(r"\b[0-9a-f]{40}\b", re.IGNORECASE),
            "internal_branch": re.compile(r"\bcodex/[A-Za-z0-9._/-]+"),
            "private_repository": re.compile(
                r"(?:github\.com|raw\.githubusercontent\.com|api\.github\.com/repos)"
                r"/vanshverma0401-wq/SetFlow(?:[/#?\s\"')]|$)", re.IGNORECASE
            ),
            "access_key": re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
            "provider_key": re.compile(r"\b(?:AIza[A-Za-z0-9_-]{30,}|sk-[A-Za-z0-9_-]{24,}|gh[pousr]_[A-Za-z0-9]{24,})\b"),
            "secret_assignment": re.compile(
                r"(?i)(?:api[_-]?key|client[_-]?secret|private[_-]?key)\s*[:=]\s*['\"][^'\"]+"
            ),
        }
        approved_emails = set(manifest().get("approved_public_emails", []))
        email_pattern = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
        findings = []
        for p in public_files():
            if p.suffix.lower() == ".png":
                continue
            content = p.read_text(encoding="utf-8")
            for label, pattern in patterns.items():
                if pattern.search(content):
                    findings.append(f"{p.relative_to(ROOT)}: {label}")
            if set(email_pattern.findall(content)) - approved_emails:
                findings.append(f"{p.relative_to(ROOT)}: unapproved email")
        self.assertFalse(findings, findings)

    def test_markdown_links_images_and_local_anchors_resolve(self) -> None:
        findings = []
        pattern = re.compile(r"(!?)\[([^\]]*)\]\((<[^>]+>|[^\s)]+)(?:\s+['\"][^)]*['\"])?\)")
        for markdown in ROOT.rglob("*.md"):
            if IGNORED_PARTS.intersection(markdown.relative_to(ROOT).parts):
                continue
            content = markdown.read_text(encoding="utf-8")
            content = re.sub(r"^\x60{3}.*?^\x60{3}[^\n]*$", "", content, flags=re.MULTILINE | re.DOTALL)
            for image, label, target in pattern.findall(content):
                parsed = urlsplit(target.strip("<>"))
                if image and not label.strip():
                    findings.append(f"{markdown.relative_to(ROOT)}: image has no alternative text")
                if parsed.scheme or parsed.netloc:
                    if parsed.scheme not in {"http", "https", "mailto"}:
                        findings.append(f"{markdown.relative_to(ROOT)}: unsupported link scheme")
                    continue
                destination = (markdown.parent / unquote(parsed.path)).resolve() if parsed.path else markdown.resolve()
                try:
                    destination.relative_to(ROOT.resolve())
                except ValueError:
                    findings.append(f"{markdown.relative_to(ROOT)}: link escapes public package")
                    continue
                if not destination.is_file():
                    findings.append(f"{markdown.relative_to(ROOT)} -> {target}")
                elif parsed.fragment and destination.suffix.lower() == ".md":
                    if unquote(parsed.fragment) not in markdown_anchors(destination.read_text(encoding="utf-8")):
                        findings.append(f"{markdown.relative_to(ROOT)} -> {target}: missing anchor")
        self.assertFalse(findings, findings)

    def test_asset_manifest_binds_reviewed_bytes_and_provenance(self) -> None:
        data = manifest()
        reviewed_on = iso_date(data["package_review_date"])
        source_reviewed_on = iso_date(data["source_review_date"])
        self.assertLessEqual(source_reviewed_on, reviewed_on)
        self.assertLessEqual(reviewed_on, date.today())
        assets = data["assets"]
        paths = [safe_relative_path(asset["path"]) for asset in assets]
        self.assertEqual(len(paths), len(set(paths)), "Duplicate asset record")
        actual = {str(p.relative_to(ROOT)) for p in public_files() if p.suffix.lower() in {".png", ".svg"}}
        self.assertEqual(set(paths), actual)
        current_captures = 0
        for asset in assets:
            with self.subTest(asset=asset["path"]):
                p = ROOT / asset["path"]
                self.assertEqual(asset["public_review"], "reviewed", "Asset needs manual public review")
                self.assertRegex(asset["sha256"], r"^[0-9a-f]{64}$")
                self.assertEqual(asset["sha256"], hashlib.sha256(p.read_bytes()).hexdigest())
                self.assertTrue(asset["description"].strip())
                if p.suffix.lower() == ".png":
                    self.assertEqual(asset["kind"], "native_simulator_capture")
                    self.assertIs(asset["synthetic_data"], True)
                    captured_on = iso_date(asset["capture_date"])
                    self.assertLessEqual(captured_on, reviewed_on)
                    self.assertEqual(iso_date(asset["source_review_date"]), source_reviewed_on)
                    self.assertIn(asset["evidence_status"], {"current", "historical"})
                    if asset["evidence_status"] == "current":
                        current_captures += 1
                        self.assertGreaterEqual(captured_on, source_reviewed_on)
                else:
                    self.assertEqual(asset["kind"], "conceptual_diagram")
        self.assertGreater(current_captures, 0, "Fresh reviewed simulator captures are required")

    def test_png_chunks_crc_and_complete_image_stream(self) -> None:
        screenshots = [p for p in public_files() if p.suffix.lower() == ".png"]
        self.assertTrue(screenshots, "No screenshots included")
        for p in screenshots:
            with self.subTest(path=str(p.relative_to(ROOT))):
                width, height = validate_png(p)
                self.assertGreaterEqual(width, 1000)
                self.assertGreaterEqual(height, 1800)

    def test_conceptual_svgs_are_valid_and_inert(self) -> None:
        svgs = [p for p in public_files() if p.suffix.lower() == ".svg"]
        self.assertTrue(svgs, "No conceptual diagrams included")
        for p in svgs:
            with self.subTest(path=str(p.relative_to(ROOT))):
                content = p.read_text(encoding="utf-8")
                self.assertNotRegex(content, r"(?i)<!DOCTYPE|<!ENTITY")
                root = ET.fromstring(content)
                self.assertTrue(root.tag.endswith("}svg") or root.tag == "svg")
                self.assertIn("conceptual", content.lower())
                self.assertIn("not an app screenshot", content.lower())
                for element in root.iter():
                    self.assertNotIn(element.tag.rsplit("}", 1)[-1].lower(), {"script", "foreignobject"})
                    for key, value in element.attrib.items():
                        local_key = key.rsplit("}", 1)[-1].lower()
                        self.assertFalse(local_key.startswith("on"), "Active SVG event attribute")
                        if local_key == "href":
                            self.assertTrue(value.startswith("#"), "External SVG reference")

    def test_public_disclosures_cover_reports_ai_and_verification_scope(self) -> None:
        readme = re.sub(r"\s+", " ", (ROOT / "README.md").read_text(encoding="utf-8"))
        evidence = re.sub(r"\s+", " ", (ROOT / "EVIDENCE_AND_LIMITATIONS.md").read_text(encoding="utf-8"))
        combined = readme + " " + evidence
        self.assertIn("REPORT_ONLY", combined)
        self.assertRegex(combined, r"restorable\s*=\s*false")
        self.assertRegex(combined.lower(), r"not\s+(?:an?\s+)?backup")
        self.assertRegex(readme.lower(), r"ai[- ](?:assisted|generated)")
        self.assertRegex(readme.lower(), r"(?:most|substantial|majority).{0,100}(?:code|implementation)|(?:code|implementation).{0,100}(?:most|substantial|majority)")
        self.assertRegex(combined.lower(), r"(?:package|documentation).{0,100}(?:checks|tests)|(?:checks|tests).{0,100}(?:package|documentation)")
        self.assertRegex(combined.lower(), r"(?:not|no|unverified|not established).{0,120}(?:release readiness|release-ready|app store)|(?:release readiness|release-ready|app store).{0,120}(?:not|unverified|not established)")
        self.assertTrue((ROOT / "ASSET_ATTRIBUTION.md").is_file())
        self.assertTrue((ROOT / "screenshots" / "README.md").is_file())

    def test_workflow_only_checks_the_local_public_package(self) -> None:
        content = (ROOT / ".github" / "workflows" / "public-package.yml").read_text(encoding="utf-8")
        self.assertIn("ubuntu-latest", content)
        self.assertIn("contents: read", content)
        self.assertIn("persist-credentials: false", content)
        self.assertIn("python3 -m unittest discover -s tests -v", content)
        self.assertNotRegex(content, r"(?i)pull_request_target|secrets\.|xcodebuild|simctl|upload-artifact|gh\s+(?:release|api|pr)")


if __name__ == "__main__":
    unittest.main()
