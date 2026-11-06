# Evidence and limitations

Source review date: **October 31, 2026**. Original local package review: **November 1, 2026**. Public presentation review: **November 6, 2026**.
The source review covers selected
implementation and test definitions in the application changes merged through
October 28, 2026, US Central time. The application source and internal execution
records remain private; this repository cannot independently reproduce them.

## How to read the evidence

| Evidence class | What it establishes | What it does not establish |
|---|---|---|
| Source/reachability evidenced | Selected code, contracts, and routes exist in the reviewed application snapshot | Fresh execution, complete correctness, or individual authorship |
| Reported verification | A dated private audit or development record reports an execution and its result | Independent reproduction in this case-study review |
| Runtime demonstrated | A dated capture or retained check shows a particular synthetic scenario running | All inputs, real-user operation, device behavior, or release readiness |
| Current development process | How coding agents are used and how the project is directed | A runtime AI feature or independent human implementation of every component |
| Future direction | A problem the product may explore | An implemented feature, delivery promise, or current result |

Implementation descriptions and personal contributions are separate claims.
Most application code was generated with AI assistance. Product direction and
workflow ownership do not imply that all implementation was independently
written or that every technical skill has been demonstrated by the owner.

## Dated verification ledger

| Date and record | Result reviewed | Scope and qualification |
|---|---|---|
| October 26, 2026, audit-v2 unit record | 1,805 recorded; 1,801 passed; zero failed; four skipped; nine special-environment tests excluded | Historical result. The audit reports 11.7% app executable-line coverage and 276 source-text checks. A large count is not equivalent behavioral coverage |
| October 26, 2026, audit-v2 UI record | 154 reported; 109 passed; 42 failed; three skipped, followed by serial triage | Historical loaded run, not a full-suite result for the later implementation |
| October 28, 2026, release/privacy change report | 1,967 tests reported; four skipped; zero failures; nine exclusions; unsigned Release archive and eight focused UI/smoke checks reported successful | Development-report evidence. Raw artifacts were not reopened during the documentation review; no signed archive, upload, or Apple acceptance is established |
| October 28, 2026, latest reviewed body-map change report | 2,176 tests reported; four skipped; zero failures; nine special-environment tests not run. A 45-test UI run initially had one failure, which passed repeated reruns | Newer author-reported local checks. Preserve the initial failure and rerun history; this is not an independently reproduced complete UI-suite pass |
| October 31, 2026, GitHub check review | Reviewed recent jobs did not start | Those statuses establish neither passing CI execution nor a code-test failure |
| October 31, 2026, source review | Selected numeric-input, unit-conversion, session-transition, body-map, readiness, permission, and guard implementations matched the described merged work | Bounded source review, not a fresh execution of every feature |

### Fresh capture evidence

The original pass captured nine fresh, visually reviewed native PNGs on October 31–November 1,
2026, in America/Chicago time, using a dedicated iPhone 17 simulator on iOS 27.0.
The final Debug build succeeded with local ad-hoc simulator signing and the
credential gate enabled. The generated simulator entitlement payload included
HealthKit and an application identity. No application source change was needed.

That historical pass remains a nine-image record. The November 6 gallery retains
seven of those images. The earlier body-model rendering and its associated
Forearms detail are omitted while their wider-distribution scope is reviewed. The original observed checks below are retained as dated history;
this presentation revision does not report a new native execution.

| Focused native check | Observed result | Limit |
|---|---|---|
| Invalid input | Weight `62.5.5` with eight valid repetitions showed an explanation and left zero of three sets completed | One specific invalid-input example; not every locale or device keyboard |
| Kilogram logging | Three sets of 62.5 kg × eight repetitions produced 1.5K kg recorded volume | Synthetic exercise fixture; not a real training or performance result |
| Rest restoration | After controlled termination/relaunch, Set 2/3 remained next and the countdown continued from 2:59 to 2:38 | Controlled termination, not hard crash, jetsam, reboot, or complete background-notification coverage |
| Retained History | After completion and another controlled relaunch, all three 62.5 kg × eight-repetition rows remained | One isolated current-store journey, not migration or all-store durability proof |
| Report preview | CSV and JSON selections both showed one candidate, one included, zero excluded, three sets, and 1.5K kg; the non-restorable qualification stayed visible | Export was not pressed; generated payload bytes and sharing were not checked |
| Builder | A separate store displayed six exercises and eighteen planned sets | This plan was not launched and did not produce the three-set demonstration |
| Recovery map | Synthetic logged history rendered chest/biceps colors; selecting Forearms opened the matching no-data sheet with no estimate and zero sets | Derived-asset rendering and one selection; not a complete accessibility or physiological validation |
| Readiness | A simulated health-history scenario displayed Based on 4 of 11 signals and a 90% rule-based example | Synthetic inputs, not actual user health observations or a clinically validated score |

These are focused native interaction checks. No native unit suite or XCTest UI
suite was run for this capture pass. Earlier test totals above remain reported
results and were not converted into new execution claims.

The first unsigned capture attempt lacked the simulator HealthKit entitlement
and failed during HealthKit access. Final selected images were recaptured with
the corrected local simulator signing configuration. This was a capture-build
correction, not an application source fix or device/distribution validation.

Exact dates, scenarios, and image descriptions are in the
[screenshot record](screenshots/README.md). The previous August gallery is
retired from this candidate. The two retained SVGs remain conceptual maps,
not application screenshots. The owner reviewed the local package and approved
publication on November 1, 2026. This approval concerns the case-study package,
not application release readiness.

## Capability boundaries

- Workout reports are versioned CSV/JSON with a `REPORT_ONLY` contract and
  `restorable=false`. They are not a backup, restore point, synchronization
  mechanism, or complete database archive.
- Progression and recovery context use rule-based logic. No trained-model
  personalization, clinical validity, or health-outcome improvement is claimed.
- Recent source work addresses earlier numeric parsing, stale-session, and
  missing-data problems. An old audit finding or an open issue alone does not
  establish that the old behavior still exists.
- Local persistence and schema evolution do not prove lossless upgrades from
  every historical installation. A genuine older shipped store was not used to
  establish that outcome in the reviewed record.
- The current scope removes the previously bundled crash/analytics SDK and
  unused generative SDK. Static privacy and release checks remain bounded
  approximations; they do not certify privacy, security, or Apple acceptance.
- Nutrition, settings, widgets, accessibility, and platform integrations have
  incomplete or unverified paths. The public story does not imply equal
  completeness across the application's surfaces.

## Publication and ownership boundaries

This source-free case study does not establish production deployment, App Store
availability, release readiness, physical-device signoff, full accessibility,
adoption, retention, revenue, or medical outcomes. It does not claim a deployed
LLM, RAG system, fine-tuned model, or autonomous coaching agent.

The public-package Python suite checks documents, links, permitted files, asset
structure, and sensitive-content patterns. It does not test the iOS application
or establish image privacy by itself. Images require visual review and known
synthetic provenance.

Application source, credentials, personal records, private execution artifacts,
and proprietary implementation details remain private. Asset provenance is
recorded separately in [asset attribution](ASSET_ATTRIBUTION.md).

Every later revision should refresh the relevant source and execution evidence.
An old image, plan, filename, or generated test definition is insufficient to
promote an unsupported claim.
