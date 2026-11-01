# SetFlow in 90 seconds

**Product:** a private, in-development native iPhone strength-training
application connecting workout planning, set logging, rest, completion, and
retained training history.

**Role:** independently directed product development with substantial
AI-assisted implementation. Vansh guides the product direction and user
workflows; AI coding agents generated most application code and also assist
with debugging, tests, and documentation.

## Start with three concrete problems

| Problem | Implemented approach | Discussion value |
|---|---|---|
| Weight input and units can change the meaning of a record | Shared numeric parsing, validation before commit, and conversion at input/display boundaries | Data correctness across a user-facing workflow |
| Interrupted workouts can leave stale resume actions | Explicit session transitions, recovery choices, and aligned Home state | Persistence, lifecycle, and failure handling |
| Missing history can look like confident guidance | No-data muscle states and readiness signal coverage | Explainable rule-based behavior and honest uncertainty |

Read the [engineering cases](../PRODUCT_DECISIONS.md) for decisions, regression
guards, and remaining limits.

## Inspect the product and proof

- [Main case study](../README.md): the product, main journey, and selected capabilities.
- [Capture index](../screenshots/README.md): screenshot dates, synthetic scenarios,
  and the exact visible states selected for review.
- [Evidence ledger](../EVIDENCE_AND_LIMITATIONS.md): source inspection, reported
  development checks, capture-specific execution, and current limitations.
- [Reusable project summary](recruiter_summary.md): a compact description for a
  longer conversation.

Recent development records report local builds and targeted tests. The reviewed
GitHub jobs did not start, so their status does not establish executed CI checks.
The public-package Python suite checks documentation and assets, not the iOS app.

## Scope

SetFlow uses Swift, SwiftUI, SwiftData, SceneKit, and HealthKit-facing data
handling. Its fitness estimates are rule-based. No App Store release,
production deployment, trained-model personalization, clinical outcome,
cross-device synchronization, or backup/restore is established by this package.
Workout reports are versioned, `REPORT_ONLY`, and non-restorable.

The useful interview conversation is a specific user flow, a decision, its
implementation evidence, the owner's actual contribution, and what remains
unverified. Application source and private development records are excluded from
this public repository.

[GitHub profile](https://github.com/vanshverma0401-wq)
