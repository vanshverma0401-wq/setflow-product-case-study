# Native simulator capture record

These nine unretouched PNGs were captured on October 31–November 1, 2026,
in **America/Chicago** time, from a dedicated iPhone 17 simulator running
iOS 27.0. Each image is 1206 × 2622 pixels. The capture build used the reviewed
application source, Debug configuration, local ad-hoc simulator signing, and
the credential gate. No application source change was needed for capture.

Every selected image was visually checked for legibility, visible state, and
synthetic provenance. The 9:41 clock and full battery are native simulator
status-bar overrides, not the capture time or an edit to the PNG. Actual dates
are listed below; exact asset hashes are in [the manifest](../public-package.json).
The owner reviewed this local package and approved publication on November 1,
2026. This approval is separate from application release validation.

## Read the scenarios correctly

**Workout journey:** an isolated three-set exercise fixture supplies the
session structure. The weight and repetition values were entered through the
UI, all three sets were logged, the report/debrief was completed, and History
was inspected after relaunch. The visible UI_TEST_AUTOMATION_SESSION note is
a fixture marker. This is a software demonstration, not an actual training
session or a performance result.

**Planning preview:** the builder uses a separate store and shows six exercises
with eighteen planned sets. It is not the setup that produced the three-set
workout. Starting and completing that eighteen-set plan was not part of capture.

**Recovery and readiness:** separate stores contain synthetic logged-history
or simulated health-observation fixtures. The readiness percentage is a
rule-based display example, not a measured physiological state or validated
prediction. The body-map imagery carries the
[derived-asset credit](../ASSET_ATTRIBUTION.md).

| Image | Capture date | Scenario | What was observed |
|---|---|---|---|
| [Workout Builder](01-workout-builder.png) | 2026-11-01 | Planning preview | Separate planning store: Chest + Triceps, six exercises and eighteen planned sets. This preview was not launched. |
| [Active workout](02-active-workout.png) | 2026-10-31 | Workout journey | Three-set synthetic Biceps fixture; set two prefills 62.5 kg and eight repetitions after the first set was logged. |
| [Rest after relaunch](03-rest-resumed.png) | 2026-10-31 | Workout journey | After controlled app termination and relaunch, the next-set context remains Set 2/3 and the clock continues from elapsed time. |
| [Saved History](04-workout-history.png) | 2026-10-31 | Workout journey | After another controlled termination and relaunch, History retains three sets of 62.5 kg × eight repetitions: 1.5K kg total. |
| [Workout report preview](05-report-preview.png) | 2026-10-31 | Workout journey | The retained demonstration workout produces one candidate, one included, zero excluded, three sets, and 1.5K kg in preview. The non-restorable qualification remains visible. |
| [Recovery body map](06-recovery-body-map.png) | 2026-10-31 | Recovery fixture | Separate synthetic history seeds chest and biceps work; the thermal view colors those regions and leaves groups without logged evidence grey. See body-model attribution. |
| [Missing-data muscle detail](07-missing-data.png) | 2026-10-31 | Recovery fixture | Selecting Forearms opens its own sheet: no estimate, zero sets, and an explanation of missing history. It does not substitute 100% recovery. |
| [Readiness signal coverage](08-readiness-coverage.png) | 2026-10-31 | Readiness fixture | Separate simulated health-history inputs show Based on 4 of 11 signals and a 90% rule-based example. These are synthetic inputs, not measured user health or clinical validation. |
| [Invalid-input feedback](09-input-validation.png) | 2026-10-31 | Workout journey | With eight valid repetitions, the entered weight 62.5.5 produces an explanation and leaves the workout at zero completed sets. Correcting it allows the later logging sequence. |

## What the focused checks establish

- Invalid weight feedback appears and blocks the attempted set start.
- Kilogram values persist from entry to later set prefills and retained History.
- Rest state and the next-set context survive controlled termination/relaunch;
  the observed countdown continues rather than restarting at three minutes.
- Completion and another relaunch retain three 62.5 kg × eight-repetition rows.
- CSV and JSON preview selection agree on one included workout and its totals.
- The recovery map renders and a Forearms selection opens the matching no-data sheet.
- Synthetic readiness inputs expose the four-of-eleven coverage qualification.

These are focused native interaction checks. No native unit suite or XCTest UI
suite was run for this capture pass. No report Export action was pressed, so
the capture pass does not establish generated payload bytes, sharing, or restore.
Controlled termination is not a hard-crash, jetsam, reboot, or migration test.
Complete accessibility, device HealthKit behavior, and release readiness remain
outside this demonstration. See [the evidence ledger](../EVIDENCE_AND_LIMITATIONS.md).

The earlier August 9 public gallery is retired from this candidate. It is not
used as evidence for the newer application changes.
