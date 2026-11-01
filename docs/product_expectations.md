# Product expectations

SetFlow is a private iPhone application in development. This case study focuses
on its training workflow and selected engineering decisions, with evidence
attached to the claims. It does not present every product surface as complete.

## Current scope

The core journey connects workout planning, set logging, rest, completion,
History, and qualified workout reports. Adjacent exercise, nutrition, hydration,
and recovery contexts have different maturity levels. Recent work emphasizes
numeric correctness, consistent units, workout continuity, and explicit missing
data. The [feature matrix](public_feature_matrix.md) records the status and
limitations of each area.

The product's progression and recovery logic is rule-based. Missing data should
remain visible, and a displayed readiness result should expose the available
signal coverage. Those design choices do not establish medical meaning or a
trained predictive model.

## What the visible proof means

A dated synthetic simulator scene shows the interface and state observed in
that scenario. It cannot establish every code path, physical-device behavior,
complete accessibility, or release readiness. The final image dates and scope
are recorded in the [screenshot record](../screenshots/README.md).

Source review and prior test reports remain separate from fresh execution.
The [evidence ledger](../EVIDENCE_AND_LIMITATIONS.md) identifies historical audit
results, later PR-reported checks, and GitHub jobs that did not execute.

## Current development process

Most application code was generated with AI coding agents. Vansh directs the
product and workflows while using substantial assistance for implementation,
debugging, tests, and documentation. Generated code and test counts do not
establish individual authorship, independent proficiency, or correctness by
themselves.

This development process is current. It is separate from future in-product AI
ideas and must not be classified as a future capability.

## Future direction

The longer-term direction is to improve continuity, explain data quality, and
explore contextual guidance that remains reviewable and under user control.
Potential LLM or retrieval extensions would need their own implementation,
evaluation, privacy boundaries, and current evidence before becoming product
claims. These themes carry no delivery date or feature promise.

## Outcomes not established here

App Store availability, production deployment, release readiness, user adoption,
revenue, medical outcomes, complete privacy/security or accessibility signoff,
cloud backup/restore, and cross-device synchronization remain unclaimed. The
workout report is explicitly non-restorable.

Each future revision should preserve these distinctions and refresh the
relevant evidence rather than carry forward an unsupported statement.
