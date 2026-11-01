# Product and engineering decisions

SetFlow explores how a training application can preserve the meaning of a user's
record across planning, input, interruptions, and review. These cases describe
implemented system decisions and their evidence. The project uses substantial
AI-generated implementation; these descriptions do not imply that every
component was independently hand-coded by the product owner.

Capability review: October 31, 2026. See the
[evidence ledger](EVIDENCE_AND_LIMITATIONS.md) for source-review dates,
author-reported checks, capture-specific execution, and remaining limits.

## 1. Preserve numeric meaning from entry to history

**Problem.** A person can enter a reasonable-looking weight that an application
parses incorrectly. Decimal separators, invalid input, unit settings, and
prefilled values all affect the saved result. An error can propagate from one
set into history, volume, and the next suggested session.

**Expected behavior.** Supported decimal formats preserve the intended number.
An invalid weight or repetition entry keeps the set open and explains the
problem. The chosen display unit stays consistent across the workflow.

**Implemented decision.** A shared parser handles supported locale separators
and Unicode decimal digits. Input validation runs before set values are
committed. Weight conversion takes place at input and display boundaries while
records retain a canonical stored unit. An untouched prefilled value preserves
its stored precision.

**Regression protection.** The project includes parser and unit-conversion
checks, invalid-input cases, and source guards for consistency across app
surfaces. Source-text guards inspect implementation patterns; they do not
execute every affected UI path.

**Evidence and limit.** Targeted source inspection supports the implementation;
later development records report local unit and focused simulator checks. Use
the [capture index](screenshots/README.md) for the exact visible input and unit
states reviewed for this case study. Device keyboards and rendered lock-screen
or Dynamic Island behavior require separate evidence.

## 2. Keep workout state and the resume interface aligned

**Problem.** The persistent workout record and the Home resume card can disagree
after an interrupted session. A stale card can offer an action that is no longer
valid, and recovery time can be mistaken for time spent training.

**Expected behavior.** A recovery choice produces a valid state transition,
updates the interface, and preserves meaningful end-time information. A failed
save retains a retryable choice. An already-ended session rejects later edits.

**Implemented decision.** The recovery path refreshes Home after a completed
choice, uses the last logged set for the recovered end time, and offers
discard-only handling for an orphan with no logged sets. A closed transition
table protects session status. Failure-aware save paths restore the affected
state without broadly rolling back unrelated work.

**Regression protection.** Targeted tests cover stale resume presentation,
zero-set recovery, recorded duration, resumed-session completion, ended-session
input refusal, and injected persistence failures.

**Evidence and limit.** The reviewed implementation and test definitions support
these decisions; development records report focused simulator success. The
case study keeps those reports separate from its own captured scenario. The
older stale-resume finding is historical context for the improvement, not a
claim that the unchanged defect remains in the reviewed implementation. This
case does not establish every interruption, crash, or device-level recovery
condition.

## 3. Show missing evidence alongside calculated guidance

**Problem.** Sparse training history can be presented as complete recovery, and
a confident readiness message can hide the fact that only a few inputs are
available. A detailed body visualization can make those estimates seem more
certain than their evidence supports.

**Expected behavior.** A muscle without relevant logged evidence shows No data.
A readiness result makes signal coverage visible. A body selection corresponds
to a defined muscle group, with an accessible alternative when the model cannot
be loaded.

**Implemented decision.** The recovery projection derives counted work from
logged sets and distinguishes missing history from a calculated fitness
estimate. Readiness exposes available-signal coverage and supports soreness
follow-up. The body view maps explicit regions to muscle groups, with selection,
accessibility, and fallback behavior developed alongside the model.

**Regression protection.** The project includes cases for untrained groups,
counted-set rules, region selection, fallback behavior, signal coverage, and
soreness follow-up. Development records retain an initial UI failure and its
rerun history; the evidence ledger does not convert that into an unconditional
full-suite pass.

**Evidence and limit.** These are rule-based fitness features. They do not
establish measured physiological recovery, medical validity, injury prevention,
or trained-model personalization. A selected image establishes its visible
state and data setup only. The body asset has derivative provenance; see the
[capture index](screenshots/README.md) and [usage terms](CASE_STUDY_USAGE.md)
for the applicable credit and boundaries.

## 4. Keep report scope explicit

A workout report answers a narrower question than a restorable application
archive. SetFlow evaluates candidate sessions, includes eligible records, and
classifies exclusions before preparing versioned CSV or JSON output.

The contract is explicitly `REPORT_ONLY` with `restorable=false`. Active,
incomplete, abandoned, malformed, future-dated, and removed records should not
silently appear as clean completed history. Historical provenance limits remain
part of the report's meaning.

A report is not a backup, restore point, or cross-device synchronization
mechanism. This boundary is illustrated in the
[conceptual report diagram](media/workout_report_boundary.svg).

## Questions for a technical discussion

- Where can user input lose meaning before it reaches a durable record?
- Which state transitions should be allowed after a workout has ended?
- How should a failed save affect the data model and the available UI actions?
- Which checks execute behavior, and which only inspect source or configuration?
- How should a fitness estimate communicate missing inputs?
- What would be needed to turn a readable report into a restorable archive?

The [evidence ledger](EVIDENCE_AND_LIMITATIONS.md) records contribution and
verification boundaries for those discussions.
