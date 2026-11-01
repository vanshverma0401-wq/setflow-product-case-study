# Frequently asked questions

## What can I evaluate in this repository?

The product problem, user journey, visible interface, selected engineering
decisions, development approach, and the evidence supporting each description.
Start with the [quick overview](docs/recruiter_quick_start.md) and the
[decision examples](PRODUCT_DECISIONS.md). The application source is private.

## How much implementation used AI?

Most application code was generated with AI coding agents. Vansh directs the
product and user workflows, with substantial agent assistance for implementation,
debugging, tests, and documentation. The case study describes system
capabilities; individual code contributions and understanding should be assessed
through specific examples and hands-on discussion.

## Is coding-agent use the same as AI inside the product?

No. AI-assisted development is the current process. Progression and recovery
features described here are rule-based. No deployed LLM, RAG system, fine-tuned
model, trained recommender, or autonomous coach is claimed.

## What do the screenshots prove?

Only the visible, dated synthetic scenarios described in the
[screenshot record](screenshots/README.md). A screenshot does not establish
complete functionality, physical-device behavior, or release readiness. The
August 9 images from the earlier package are retired from this candidate. The
new gallery uses nine native captures from October 31–November 1, 2026, with
separate synthetic workout, planning, recovery, and readiness scenarios.

## What was freshly executed for this update?

A Debug simulator build, credential gate, and focused native interactions:
invalid-input refusal, three-set kilogram logging, controlled rest relaunch,
completion, retained History after another relaunch, CSV/JSON preview selection,
a separate Builder preview, recovery-map rendering/selection, and synthetic
readiness coverage. No native unit or XCTest UI suite was run for capture.
The [evidence ledger](EVIDENCE_AND_LIMITATIONS.md) records the exact limits.

## Is the whole application tested and passing?

That claim is not made. The reviewed record contains dated audit runs and newer
PR-reported local checks with skips, exclusions, and a UI failure/rerun history.
The recent GitHub jobs inspected did not start. The
[verification ledger](EVIDENCE_AND_LIMITATIONS.md) preserves those distinctions.

## What do this repository's Python tests cover?

The public package: its documents, links, permitted files, and selected asset
and sensitive-content checks. They do not execute or validate the iOS app.
Manual visual and privacy review is still required for images.

## Can the workout export restore my data?

No. CSV and JSON exports have a versioned `REPORT_ONLY` contract and
`restorable=false`. They are readable workout reports, not a database backup,
restore point, or cross-device synchronization mechanism.

## Is SetFlow available in the App Store?

This is a private in-development product case study. It makes no App Store
availability, production deployment, beta-readiness, or release-readiness claim.
An unsigned archive or static readiness check does not establish distribution.

## Are the health and recovery features medical advice?

No clinical interpretation, medical advice, injury prevention, or measured
health outcome is claimed. The product is fitness-oriented, with explicit
boundaries around missing and incomplete data.

## Did SetFlow create the body model entirely from scratch?

No. The app's current model notice describes a derived asset combining
MakeHuman surface data with Z-Anatomy/BodyParts3D-derived material. Credits,
sources, modifications, and license scope are in
[asset attribution](ASSET_ATTRIBUTION.md). The raw model is not included here.

## What remains outside this public case study?

Application source, credentials, user records, private execution artifacts, and
unreleased implementation plans. Physical-device validation, complete
accessibility, production performance, adoption, revenue, privacy/security
signoff, and release acceptance each require separate current evidence.
