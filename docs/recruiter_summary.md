# Recruiter summary

## Project description

SetFlow is a private iOS strength-training application in active development.
It connects session planning, weight and repetition entry, timed rest,
completion feedback, and retained workout history. Adjacent recovery,
nutrition, hydration, progress, and preference surfaces extend the training
context with different maturity levels.

I direct the product and its user workflows, with substantial AI assistance for
implementation, debugging, tests, and documentation. Most application code was
generated with AI coding agents. The case study describes the resulting system;
specific implementation contributions and technical understanding are best
explored through concrete examples.

## Technical discussion areas

- **Data correctness:** supported decimal formats, invalid-input refusal, weight
  conversion, and consistency between entered and retained values.
- **Application lifecycle:** session transitions, rest restoration,
  interrupted-workout recovery, and retryable persistence failures.
- **Evidence-aware fitness context:** missing-data muscle states, readiness
  signal coverage, and the boundary between a rule-based estimate and a
  physiological measurement.
- **Local data and portability:** SwiftData-backed records and versioned CSV/JSON
  workout reports with explicit eligibility and non-restorable semantics.
- **Verification practice:** source review, targeted regression guards, reported
  local checks, visible simulator evidence, and the limits of each layer.

## Evidence and current scope

The public package includes [product decisions](../PRODUCT_DECISIONS.md), a
[dated evidence ledger](../EVIDENCE_AND_LIMITATIONS.md), and a
[capture index](../screenshots/README.md) for the selected simulator states.
Earlier development records report local builds and targeted tests. Reviewed
GitHub jobs did not start; a job status alone is not executed verification.

SetFlow is in development. This case study establishes no App Store release,
production adoption, revenue, physical-device signoff, medical outcome, or
trained-model personalization. Coding with AI is a development-process
disclosure; it does not establish an in-product LLM or autonomous coach.

Workout reports are `REPORT_ONLY` with `restorable=false`: a report is not a
backup, restore point, or synchronization mechanism. Application source,
credentials, personal data, and private development records remain private.

For a fast first pass, use the [90-second overview](recruiter_quick_start.md).

[GitHub profile](https://github.com/vanshverma0401-wq)
