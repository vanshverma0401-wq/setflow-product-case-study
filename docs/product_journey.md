# Product journey

## 1. Orient

Home is the entry point for the current training context. The user can move from
the shared product shell into workout planning while wellness, fuel, progress,
history, and profile contexts remain separately accessible.

Product principle: adjacent information should be discoverable without implying
that every domain is equally complete or can be reduced to one score.

## 2. Plan

The workout-building flow gives structure to the upcoming session. Before a new
session begins, the product checks whether another active session already exists.

Product principle: continuity and destructive transitions should be explicit.
An existing session can be resumed or deliberately abandoned instead of being
silently replaced.

## 3. Execute

The private product contains an active-workout experience. This case study keeps
the implementation and internal route details private, so it presents the state
decision rather than source code.

Product principle: live execution is stateful. Planning, starting, resuming, and
ending should not be treated as unrelated screens.

## 4. Review and export

Completed eligible workout records can be prepared as CSV or JSON reports. The
contract is versioned and explicitly marked `REPORT_ONLY` with
`restorable=false`.

Product principle: a readable report is not a database archive. A user should
not mistake export for backup, restore, or synchronization.

## 5. Continue with context

Wellness, Fuel, Pilot, Data, and Profile keep complementary context within the
same shell. Their presence supports a broader training journey, but this public
revision does not claim equal completeness, clinical meaning, or public runtime
proof for every surface.

## Trust boundary across the journey

If persistent storage becomes degraded, temporary or recovery state should be
visible instead of silently appearing durable. This trust principle connects
product copy, state design, persistence handling, and export language.

For the precise evidence attached to each statement, see the
[public feature matrix](public_feature_matrix.md).

