# Evidence and limitations

## Evidence model

Public statements in this case study were checked against a clean, committed
private-source snapshot. The review separated four types of evidence:

1. **Source evidence** — a feature or contract exists in compiled-target source.
2. **Reachability evidence** — a route connects the feature to the primary app
   shell or another reachable product surface.
3. **Runtime evidence** — an exact build or UI path was observed running.
4. **Release evidence** — signing, distribution, privacy, device, and store gates
   are complete.

This public package relies on verified source and reachability evidence. It does
not use those checks to claim release readiness.

## Verified statements

- The application is built with Swift, SwiftUI, and SwiftData.
- The primary shell routes to Home, Wellness, Fuel, Pilot, Data, and Profile.
- Home reaches a workout-building flow.
- The private source contains an active-workout experience.
- The report surface generates CSV and JSON workout reports.
- The report contract is versioned, `REPORT_ONLY`, and non-restorable.
- The application models explicit degraded-storage and recovery states.

## Statements intentionally excluded

- App Store availability or production deployment
- release readiness or full device/privacy signoff
- backup or restore capability
- cross-device or cloud synchronization
- medical or health-outcome claims
- a deployed LLM, retrieval-augmented generation system, fine-tuned model, or
  autonomous coaching agent
- public source availability
- proprietary architecture and service details
- secrets, monetization details, and unreleased plans

## Screenshot boundary

Five iOS Simulator screenshots are included after a separate privacy review.
They show Home, Workout Hangar, Fuel, Pilot, and Profile in demo/test state and
do not contain a real user's account, health, or workout data. They establish
only the visible interface represented in those images. Wellness and Data are
supported by source and route evidence but are not represented by public runtime
captures in this revision.

The two included SVGs are conceptual product maps. They are not replicas of the
private UI and do not establish runtime behavior.

## Development-process boundary

AI assistance is used in the engineering workflow for problem decomposition,
implementation options, debugging, documentation, and audit support. This is a
process statement, not source, runtime, or release evidence. Suggestions remain
subject to human review and proportional verification; generated output is not
treated as proof.

## Evidence freshness

The case study reflects one verified private-source snapshot. Product work can
continue after that point, so future edits must recheck every feature statement
against the then-current clean source before publication.
