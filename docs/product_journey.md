# Product journey

SetFlow connects planning, live workout state, and the resulting record. This
journey explains the product behavior; the
[feature matrix](public_feature_matrix.md) and
[evidence ledger](../EVIDENCE_AND_LIMITATIONS.md) attach the relevant evidence
and limitations. Selected visual states are documented in the
[capture index](../screenshots/README.md).

## 1. Plan a session

The user chooses exercises, muscle targets, equipment, goals, duration, and
session structure. The entry flow checks for an existing active workout before
starting another. Resolving that session is an explicit user choice.

The product aim is continuity: planning should agree with the workout that is
actually active.

## 2. Record the work

During a session, the user enters weight and repetitions and records completed
sets. Supported decimal formats and the chosen weight unit affect how the input
is interpreted. Invalid input should keep the set open with understandable
feedback, rather than silently create an unintended record.

The [numeric-input case](../PRODUCT_DECISIONS.md#1-preserve-numeric-meaning-from-entry-to-history)
explains validation and unit handling.

## 3. Rest and return

Rest periods belong to the active session. Locally retained state supports
returning to the same workout, while elapsed-time handling accounts for time
away from the app.

Interrupted-session recovery has its own state choices and save-failure
handling. Completing or discarding a recovered session should update the Home
interface, and an ended session should remain ended. The
[continuity case](../PRODUCT_DECISIONS.md#2-keep-workout-state-and-the-resume-interface-aligned)
explains these rules and their proof limits.

## 4. Complete and review

Completion leads to feedback and a debrief, with the workout retained in History.
Users can inspect exercises, sets, recorded volume, session feedback, and
personal records. A past workout can be repeated through the cloning flow.

History is the point where the planned session and actual recorded work must
remain distinguishable. The current case study does not imply that every
completion, editing, template, or partial-workout scenario is implemented.

## 5. Generate a qualified report

Eligible completed workout records can be prepared as versioned CSV or JSON.
The report describes its included and excluded scope and is marked
`REPORT_ONLY` with `restorable=false`.

A report is not a backup. It cannot restore the application database or
synchronize another device. The
[report-boundary diagram](../media/workout_report_boundary.svg) explains this
contract.

## 6. Continue with fitness context

The recovery view connects logged training history to rule-based muscle
estimates and exposes No data where relevant evidence is absent. Readiness
communicates signal coverage. Nutrition, hydration, progress, and preferences
remain adjacent product areas with different maturity levels.

Fitness context does not establish a medical measurement, clinical outcome, or
trained prediction. The [missing-data case](../PRODUCT_DECISIONS.md#3-show-missing-evidence-alongside-calculated-guidance)
explains the distinction between an absent input and a calculated estimate.

## Trust across the journey

Input errors, failed saves, incomplete data, and degraded persistence affect the
user's understanding of the product. Those states belong in the interface and
in the public evidence record. A screenshot demonstrates only the state shown;
source inspection, reported test results, capture-specific execution, and device
or distribution validation remain separate evidence layers.
