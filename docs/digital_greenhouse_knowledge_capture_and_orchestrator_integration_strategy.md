# Digital Greenhouse Knowledge Capture and Orchestrator Integration Strategy

## 1. Purpose of this document

This document explains how the future digital greenhouse should be integrated with the Agro Decision Orchestrator (Agro-DO).

Its purpose is to align three things that must remain connected but clearly separated:

1. expert greenhouse knowledge capture,
2. structured digital greenhouse modeling,
3. decision-oriented runtime context for Agro-DO.

This document also explains why the first greenhouse template should be intentionally exhaustive, why that is not a problem, and how the real criterion for refinement should be the quality of Agro-DO behavior in complex real decision cases.

This is not yet the greenhouse template itself.  
This is the conceptual and methodological guide that explains how that template should be used, why it matters, and how it should ultimately feed the orchestrator.

---

## 2. Core idea

The main question is not whether the greenhouse knowledge template should contain 40 fields or 140 fields.

That matters, but it is not the decisive issue.

The decisive issue is this:

**When Agro-DO receives a complex real case, does the captured greenhouse context provide enough structured information for the orchestrator to reason correctly?**

That is the real quality test.

For that reason, the integration should not be designed as a single flat template that feeds the orchestrator directly.  
It should be designed as a three-layer system:

1. exhaustive knowledge capture,
2. canonical digital greenhouse model,
3. decision-oriented runtime payload.

This separation is essential.

---

## 3. Why the first template should be exhaustive

At the beginning of the project, the greenhouse knowledge template should be deliberately rich and highly detailed.

That is the correct choice for three reasons.

### 3.1 It prevents loss of expert knowledge

The domain expert may hold important details that initially seem excessive, but later become critical for decision quality.

Examples include:
- structural constraints,
- winter snow-load concerns,
- drainage layouts,
- manual intervention practices,
- actuator limitations,
- fallback routines,
- sector priority logic,
- hidden dependencies between infrastructure elements,
- real operational trade-offs,
- or recovery procedures known only from experience.

If these details are not captured early, they may be lost or remembered only partially later.

### 3.2 It allows later simplification without early damage

A rich template can always be simplified later.  
A poor template cannot recover knowledge that was never captured.

This means that over-capture is safer than under-capture in the first phase.

### 3.3 It makes refinement evidence-driven

The template should not be simplified because it “looks too long.”  
It should only be simplified or refined when the team has evidence that some parts do not improve decision quality.

That evidence should come from observing Agro-DO behavior in difficult cases, not from intuition alone.

---

## 4. The most important principle

The greenhouse template should not be optimized for elegance.

It should be optimized for **decision usefulness**.

The right question is not:

- “Is the template too detailed?”

The right question is:

- “When Agro-DO faces a complex case, what information did it actually need in order to reason well?”

This changes the whole design philosophy.

The template is not the final product.  
The template is a knowledge-capture instrument that supports the creation of a better digital greenhouse model, which in turn supports better decision behavior.

---

## 5. Recommended integration architecture

The integration should be built around three separate but connected artifacts.

## 5.1 Layer 1 — Expert knowledge capture

This is where the domain expert describes the greenhouse as fully as needed.

The format can be a rich markdown template or interview-driven structured document.

Its function is:
- to capture expert reality,
- to preserve nuance,
- to collect structural, operational, agronomic, and recovery knowledge,
- and to avoid early simplification.

At this stage, natural language is acceptable and expected.

This layer may include:
- greenhouse geometry,
- structure type,
- drainage systems,
- snow-load considerations,
- vents,
- actuator systems,
- irrigation logic,
- boiler room and technical room information,
- operational routines,
- fallback procedures,
- agronomic priorities,
- failure patterns,
- and real-world trade-offs.

This layer is intentionally rich.

## 5.2 Layer 2 — Canonical digital greenhouse model

This layer converts the captured knowledge into a clean structured representation.

This is the actual digital greenhouse blueprint.

It should not remain as free text.  
It should become a normalized, machine-usable model that can be queried and used by Agro-DO.

This model should represent at least:

- assets,
- topology,
- sectors or zones,
- resource flows,
- operational constraints,
- fallback paths,
- priorities,
- failure modes,
- and recovery options.

This layer is where expert narrative becomes a stable operational model.

## 5.3 Layer 3 — Decision-oriented runtime payload

This is the layer used when Agro-DO evaluates a case.

The orchestrator should not receive the entire raw knowledge template every time.  
It should receive a relevant contextual payload derived from:

- the greenhouse blueprint,
- the current case,
- the active signals,
- the affected assets,
- the sector priorities,
- and the currently relevant constraints or recovery options.

This layer is dynamic and case-specific.

Its purpose is to give Agro-DO the context it needs for the current decision, without overloading it with irrelevant detail.

---

## 6. Why these three layers must remain separate

If these layers are mixed together, two problems appear immediately.

### 6.1 If the template is too poor

Important expert knowledge gets lost and later decisions become shallow or unrealistic.

### 6.2 If the orchestrator receives raw exhaustive context directly

It becomes overloaded with detail that may not be relevant for the current case.

That reduces clarity and increases the risk of weak reasoning.

The separation therefore protects both:
- knowledge richness,
- and decision clarity.

---

## 7. What the digital greenhouse should ultimately contain

The final digital greenhouse should not be just a document.  
It should become a structured operational model.

At minimum, it should capture the following classes of information.

## 7.1 Asset layer
Examples:
- tanks,
- pumps,
- pipes,
- valves,
- controllers,
- climate actuators,
- ridge vents,
- sensors,
- boilers,
- technical-room elements,
- emergency supply interfaces.

## 7.2 Topology layer
Examples:
- which assets feed which circuits,
- which valves affect which sectors,
- which pumps support which lines,
- what dependencies exist between structural or operational subsystems.

## 7.3 Sector layer
Examples:
- sectors,
- agronomic grouping,
- priority ranking,
- tolerance to stress,
- production criticality,
- continuity hierarchy.

## 7.4 Resource layer
Examples:
- water reserves,
- hydraulic capacity,
- power dependencies,
- backup resources,
- temporary supply alternatives.

## 7.5 Constraint layer
Examples:
- structural limits,
- seasonal constraints,
- snow-load concerns,
- pressure limitations,
- manual intervention bottlenecks,
- connection delays,
- operational safety boundaries.

## 7.6 Failure-mode layer
Examples:
- pump degradation,
- valve failure,
- tank depletion,
- sensor drift,
- communication loss,
- hydraulic instability,
- recovery-path unavailability.

## 7.7 Recovery-path layer
Examples:
- backup lines,
- tanker supply,
- emergency refill procedures,
- staged restart routines,
- degraded continuity strategies.

## 7.8 Runtime state layer
Examples:
- current levels,
- pressure,
- flow,
- alarms,
- sensor trust,
- active overrides,
- operator constraints,
- current continuity feasibility.

---

## 8. How Agro-DO should use the digital greenhouse

Agro-DO should not treat the greenhouse as a static descriptive object.

It should use the digital greenhouse as a contextual reasoning substrate.

In practice, this means:

1. the greenhouse blueprint defines what exists and how it works,
2. the runtime state defines what is currently happening,
3. the case defines what problem must be evaluated,
4. and Agro-DO uses both together to produce the recommendation.

This is where the system becomes powerful.

The orchestrator stops being a generic case classifier and becomes a context-aware operational decision-support service.

---

## 9. How the team should refine the template over time

The greenhouse knowledge template should be refined through iteration, not theory.

The correct cycle is this:

1. capture rich greenhouse knowledge,
2. build or improve the structured blueprint,
3. run difficult decision cases,
4. observe Agro-DO behavior,
5. identify missing or unnecessary context,
6. refine the template only where evidence justifies it.

This means the template evolves through real decision performance.

That is the right method.

---

## 10. The real criterion for template quality

The real measure of success is not whether the template looks complete.

The real measure is whether Agro-DO performs well in complex cases.

A good template is one that helps the digital greenhouse provide enough context for the orchestrator to:

- distinguish between continuity and interruption,
- prioritize correctly,
- recognize collapse boundaries,
- identify credible recovery paths,
- avoid shallow or generic recommendations,
- and remain aligned with real operational logic.

If the orchestrator fails, the team should ask:

- Was a critical physical dependency missing?
- Was a sector priority missing?
- Was a recovery path missing?
- Was an operational constraint missing?
- Was a failure mode poorly represented?
- Was irrelevant detail hiding the important signals?

That is how refinement should happen.

---

## 11. Recommended working approach with the domain expert

The domain expert should continue describing the greenhouse in as much detail as needed.

The team should not force early compression.

The recommended process is:

### Step 1
Keep collecting greenhouse knowledge through a rich template.

### Step 2
Translate each completed section into structured model elements.

### Step 3
Use the structured greenhouse blueprint in Agro-DO case generation and runtime payload construction.

### Step 4
Run realistic complex cases.

### Step 5
Refine the template only where Agro-DO behavior reveals missing or unhelpful context.

This preserves expert value while keeping the integration disciplined.

---

## 12. Recommended artifact set

To implement this approach cleanly, the project should explicitly maintain three separate artifacts.

### 12.1 `greenhouse_knowledge_capture_template.md`
Purpose:
- expert knowledge capture,
- exhaustive domain input,
- interview and documentation support.

### 12.2 `greenhouse_blueprint.schema.json`
Purpose:
- normalized target structure for the digital greenhouse,
- machine-usable representation of assets, sectors, constraints, and recovery paths.

### 12.3 `decision_case.schema.json`
Purpose:
- case-level operational payload structure for Agro-DO,
- dynamic decision context derived from the blueprint plus runtime conditions.

This separation will reduce confusion and make the whole architecture more scalable.

---

## 13. Recommended immediate next step

The next practical step should be:

**Create the first full version of the greenhouse knowledge capture template, already designed so that it can later be translated into a structured greenhouse blueprint for Agro-DO.**

That is the correct next move because it turns the current conceptual agreement into a reusable working instrument.

---

## 14. Final conclusion

The important issue is not whether the first greenhouse template is too detailed.

The important issue is whether the captured context allows Agro-DO to behave well in complex real decision situations.

For that reason:

- early capture should be exhaustive,
- the digital greenhouse should be normalized separately,
- the orchestrator should consume only relevant runtime context,
- and the template should be refined through observed decision performance.

This is the right path for integrating the future digital greenhouse with Agro-DO in a technically serious and scalable way.
