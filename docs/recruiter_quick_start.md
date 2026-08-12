# SetFlow in 90 seconds

## What it is

SetFlow is my private in-development iOS strength-training product. It connects
workout planning and live-session continuity with wellness, fuel, progress,
history, data, and profile context in one product shell.

It is being built toward a trustworthy training operating system with reviewable
contextual guidance, explicit uncertainty, durable-history protection, and user
control. That direction is not presented as a shipped AI feature.

## What I owned

I worked independently across product framing, SwiftUI interaction and
navigation, workout state, SwiftData persistence decisions, report boundaries,
failure-state communication, validation, AI-assisted development under human
review, and the privacy-conscious case study.

## Two decisions worth discussing

1. **Active-session continuity:** the entry flow checks for an existing session
   and requires the user to resume it or deliberately abandon it before starting
   another.
2. **Reports are not backups:** CSV and JSON workout reports are versioned,
   filtered for eligibility, and explicitly labeled `REPORT_ONLY` and
   non-restorable.

## Visual proof

Five privacy-reviewed simulator captures in the [main case study](../README.md)
show Home, Workout Hangar, Fuel, Pilot, and Profile in demo/test state. Two
conceptual diagrams explain the product system and export boundary without
exposing source or proprietary architecture.

## Honest boundary

The package does not claim App Store availability, production deployment,
release readiness, cross-device sync, backup/restore, adoption, revenue, or
health outcomes. The full split between demonstrated behavior, private-source
evidence, future direction, and non-claims is in
[product expectations](product_expectations.md).

## Good interview follow-ups

- How should a product handle an already-active workout?
- What makes a data report different from a restorable archive?
- How do degraded persistence states affect user trust?
- How can private-source work still be evaluated responsibly?
- How should coding-agent suggestions be verified before they become durable
  product decisions?
- What evidence would be required before describing contextual guidance as a
  shipped AI feature?
