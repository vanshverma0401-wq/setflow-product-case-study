# Product decisions

## 1. One product shell, explicit domains

SetFlow uses one primary navigation shell for Home, Wellness, Fuel, Pilot, Data,
and Profile. The decision is not to blend all information into one score. Each
area owns a different part of the experience while remaining reachable from a
consistent shell.

Why it matters:

- users do not have to learn a different navigation model for every context
- adjacent data remains discoverable without losing domain-specific meaning
- incomplete signals can remain visibly incomplete instead of being hidden by a
  universal dashboard number

## 2. Active-session continuity before new-session convenience

The workout entry flow checks for an existing active session. When one exists,
the user can resume it or deliberately abandon it before starting another.

Why it matters:

- prevents two accidental concurrent workout states
- makes a destructive transition explicit
- keeps the planning surface aligned with live execution state

## 3. Reports are not backups

The workout-report flow previews candidate, included, and excluded session
counts before generating CSV or JSON. The export contract is versioned and
explicitly non-restorable.

Why it matters:

- a readable report and a restorable application archive are different products
- eligibility rules keep active, incomplete, abandoned, malformed, future-dated,
  or removed records out of an apparently clean historical report
- clear contract language reduces the chance that users mistake a report for a
  recovery mechanism

## 4. Degraded persistence must be visible

The private implementation distinguishes normal persistent storage, in-memory
fallback, pending recovery choice, and minimal recovery states.

Why it matters:

- temporary state should not look durable
- failure handling should not silently delete data
- warnings and recovery choices are part of the user experience, not only error
  logging concerns

## 5. Public proof can remain useful without public source

This case study publishes the problem, decisions, verified feature boundaries,
limitations, and conceptual diagrams while keeping the implementation private.

Why it matters:

- recruiters can evaluate product and engineering judgment
- users, credentials, architecture, and unreleased work remain protected
- every public statement stays bounded by evidence rather than roadmap intent

