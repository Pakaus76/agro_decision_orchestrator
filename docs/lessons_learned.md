# Lessons Learned

## Purpose of this file
This file captures stable working rules and reusable project lessons that should influence future interactions, implementation steps, documentation discipline, and handoffs.

## Lessons

### [LESSON-004]
**Title:** Manager summaries must be cumulative without repeating the same wording

**Rule to preserve**  
Project-manager summaries must accumulate progress and explain the delta of the current milestone. They should not mechanically repeat the same introduction or the same sequence of ideas at each update.

### [LESSON-005]
**Title:** Product projects must not inherit experimental version ladders from thesis repositories

**Context**  
During the first attempt to create orchestration logic, the project briefly drifted toward a thesis-style naming pattern such as `condition_a.py`, inherited from the previous industrial research repository.

**Rule to preserve**  
This agricultural project must be built as one real Agro-DO product. Internal implementation steps may exist, but they must not be framed, named, or documented as visible benchmark conditions or product variants such as A/B/C/D/E/F.

**Why this matters**
- protects the product identity
- avoids research-oriented drift
- keeps the architecture aligned with a future service that can be deployed and monetized
