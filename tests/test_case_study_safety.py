from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SCREENSHOTS = {
    "01-home.png",
    "02-hangar.png",
    "03-fuel.png",
    "04-pilot.png",
    "06-profile.png",
}


def files() -> list[Path]:
    return sorted(path for path in ROOT.rglob("*") if path.is_file())


def test_package_contains_no_application_source_or_binary() -> None:
    forbidden_suffixes = {
        ".swift",
        ".xcodeproj",
        ".xcworkspace",
        ".plist",
        ".entitlements",
        ".app",
        ".ipa",
        ".dSYM",
        ".sqlite",
        ".store",
    }
    assert not [path for path in files() if path.suffix in forbidden_suffixes]


def test_no_private_checkout_or_secret_patterns() -> None:
    patterns = {
        "absolute_home_path": re.compile(r"/(?:Users|Volumes|home)/[^\s`]+"),
        "git_commit_hash": re.compile(r"\b[0-9a-f]{40}\b", re.IGNORECASE),
        "internal_branch": re.compile(r"\bcodex/[A-Za-z0-9._/-]+"),
        "access_key": re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
        "generic_secret": re.compile(r"(?i)(api[_-]?key|client[_-]?secret|private[_-]?key)\s*[:=]\s*['\"][^'\"]+"),
        "email": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE),
    }
    findings: list[str] = []
    for path in files():
        if path.name == "test_case_study_safety.py":
            continue
        if path.suffix.lower() == ".png":
            continue
        content = path.read_text(encoding="utf-8", errors="ignore")
        for label, pattern in patterns.items():
            if pattern.search(content):
                findings.append(f"{path.relative_to(ROOT)}: {label}")
    assert not findings, findings


def test_required_public_boundaries_are_explicit() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    required = [
        "private in-development product",
        "not an App Store release",
        "REPORT_ONLY",
        "restorable=false",
        "not a backup",
        "Cross-device synchronization is not claimed",
        "five product images are privacy-reviewed iOS Simulator captures",
        "two diagrams are conceptual product maps, not app screenshots",
        "not App Store availability, production deployment, or release readiness",
    ]
    assert all(text in readme for text in required)


def test_markdown_links_and_images_resolve() -> None:
    missing: list[str] = []
    for markdown in ROOT.rglob("*.md"):
        content = markdown.read_text(encoding="utf-8")
        for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", content):
            if re.match(r"^[a-z]+://", target, re.IGNORECASE) or target.startswith("#"):
                continue
            if not (markdown.parent / target.split("#", 1)[0]).is_file():
                missing.append(f"{markdown.relative_to(ROOT)} -> {target}")
    assert not missing, missing


def test_svgs_are_valid_and_labeled_conceptual() -> None:
    svgs = sorted((ROOT / "media").glob("*.svg"))
    assert len(svgs) == 2
    for path in svgs:
        ET.parse(path)
        content = path.read_text(encoding="utf-8")
        assert "Conceptual" in content
        assert "not an app screenshot" in content.lower()


def test_public_screenshots_have_exact_names_and_valid_png_headers() -> None:
    screenshots = sorted((ROOT / "screenshots").glob("*.png"))
    assert {path.name for path in screenshots} == EXPECTED_SCREENSHOTS
    for path in screenshots:
        header = path.read_bytes()[:24]
        assert header[:8] == b"\x89PNG\r\n\x1a\n"
        width = int.from_bytes(header[16:20], "big")
        height = int.from_bytes(header[20:24], "big")
        assert width >= 1000 and height >= 1800, (path.name, width, height)
        assert path.stat().st_size < 5_000_000


def test_exact_candidate_file_contract() -> None:
    assert len(files()) == 15
    assert all(path.stat().st_size < 5_000_000 for path in files())
