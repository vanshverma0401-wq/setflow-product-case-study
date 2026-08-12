# Product expectations and evidence map

This document explains how to read the SetFlow case study. It is a product and
engineering record for a private in-development application, not a release page.

## Runtime demonstrated

Five privacy-reviewed iOS Simulator captures show the visible Home, Workout
Hangar, Fuel, Pilot, and Profile surfaces in demo/test state. They demonstrate
only what appears in those images and the shared shell visible across them.

They do not establish real-user deployment, physical-device behavior, complete
accessibility, end-to-end privacy, distribution readiness, or every internal
state of the product.

## Source/reachability evidenced

A reviewed private-source snapshot supports the following bounded statements:

- Swift, SwiftUI, and SwiftData are used in the application.
- the primary shell routes to Home, Wellness, Fuel, Pilot, Data, and Profile;
- Home reaches structured workout planning;
- the private product contains an active-workout experience;
- workout reports can be produced as versioned CSV and JSON;
- the report contract is `REPORT_ONLY` and `restorable=false`;
- degraded-storage and recovery states are modeled explicitly.

Source and reachability evidence show that a path exists in the reviewed
snapshot. They are not substitutes for fresh runtime, device, privacy, or
release validation.

## Future direction

The public direction is intentionally thematic:

- make the plan-to-session-to-review journey more coherent;
- make data durability and report boundaries easier to understand;
- improve how workout, wellness, fuel, progress, history, and profile context
  complement one another without collapsing them into one unsupported score;
- explore contextual intelligence that can surface reviewable guidance with
  rationale, uncertainty, and user control while preserving durable history;
- expand verification and presentation only when the supporting evidence is
  current and safe to share.

These themes are not feature promises, schedules, or a disclosure of unreleased
implementation plans.

## AI-assisted engineering process

AI assistance is part of the product-development workflow, not a runtime feature
claim. It supports problem decomposition, implementation options, debugging,
documentation, and evidence review. Human inspection and proportional build,
test, runtime, and source checks remain the decision gates.

This process statement does not establish that AI-generated output is correct,
that every suggestion is accepted, or that SetFlow currently ships an LLM or
autonomous coach.

## Not claimed

This case study does not claim:

- App Store availability, production deployment, or release readiness;
- active users, adoption, retention, revenue, or commercial results;
- physical-device, full accessibility, privacy, security, or performance
  signoff;
- cloud backup, restore, or cross-device synchronization;
- medical advice, clinical interpretation, or health outcomes;
- a deployed LLM, retrieval-augmented generation system, fine-tuned model, or
  autonomous coaching agent;
- public source availability or a complete architecture disclosure.

## Expectation for future revisions

Every revision must preserve the distinction above. If a current review cannot
re-establish a statement, the statement should be softened or removed rather
than carried forward from an older screenshot or plan.
