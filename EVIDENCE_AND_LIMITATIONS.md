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
- public source availability
- proprietary architecture and service details
- secrets, monetization details, and unreleased plans

## Screenshot boundary

The included SVGs are conceptual product maps. They are not replicas of the
private UI. No simulator screenshot is included because screenshots require a
separate review for personal information, health information, account content,
internal feature states, and unreleased design details.

## Evidence freshness

The case study reflects one verified private-source snapshot. Product work can
continue after that point, so future edits must recheck every feature statement
against the then-current clean source before publication.

