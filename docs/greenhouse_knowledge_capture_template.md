# Greenhouse Knowledge Capture Template

## 1. Purpose of this template

This template is designed to capture expert greenhouse knowledge in a structured and exhaustive way so that it can later be transformed into a usable digital greenhouse model for Agro Decision Orchestrator (Agro-DO).

This is **not** the final machine-readable greenhouse blueprint.  
This is the expert-facing capture layer.

Its purpose is to preserve detailed operational knowledge before simplification, normalization, and schema conversion.

Use this template to collect as much relevant information as possible from the domain expert. It is acceptable for some sections to remain partially empty at first and be completed iteratively.

---

## 2. How to use this template

### Recommended working method
- Fill the template progressively, not all at once.
- Prefer rich detail over premature simplification.
- Keep the expert wording when it contains operational meaning.
- Mark uncertainty explicitly instead of guessing.
- Add examples, exceptions, seasonal constraints, and real-world practices whenever relevant.
- If a section does not apply, write `Not applicable` and explain why.

### Important principle
This template is not judged by how elegant it looks.  
It is judged by whether it helps Agro-DO reason correctly in future complex cases.

---

## 3. Document metadata

### 3.1 Capture session metadata
- Template version:
- Document date:
- Interview / input session date:
- Expert name:
- Expert role:
- Recorder / editor:
- Greenhouse identifier:
- Site name:
- Country:
- Region / nearest city:
- Notes on source reliability:

### 3.2 Scope of current capture
- What part of the greenhouse is covered in this session?
- What is still missing?
- What topics need later clarification?
- What assumptions are currently provisional?

---

## 4. Business and operational purpose of the greenhouse

### 4.1 Business intent
- Main crops:
- Main commercial objective:
- Production model:
- Main customer / market type:
- Yield sensitivity:
- Cost sensitivity:
- Quality sensitivity:
- Time-critical production windows:

### 4.2 Operational intent
- Main operating philosophy:
- Main continuity objective:
- What must almost never fail?
- What can be degraded temporarily?
- What is acceptable to stop first under constraint?
- What is never acceptable to stop without escalation?

---

## 5. Site and environmental context

### 5.1 Site description
- Site location:
- Land size:
- Terrain description:
- Slope:
- Drainage characteristics:
- Soil characteristics relevant to infrastructure:
- Access limitations:
- Logistics constraints:

### 5.2 Environmental context
- Typical climate:
- Seasonal temperature range:
- Rain characteristics:
- Wind exposure:
- Snow / frost exposure:
- Storm exposure:
- Known environmental risks:
- Seasonal operating challenges:

### 5.3 External dependencies
- External water sources:
- External power dependencies:
- Road access limitations:
- Dependence on tanker logistics:
- Neighboring shared infrastructure:
- Utility vulnerability:

---

## 6. Greenhouse general description

### 6.1 General configuration
- Greenhouse type:
- Structure family:
- Covering type:
- Technology level:
- Number of tunnels / bays:
- Width per tunnel:
- Length per tunnel:
- Total covered area:
- Maximum height:
- Gutter height:
- Ridge / zenith height:
- Orientation:
- Number of operational sectors:
- Number of agronomic sectors:

### 6.2 Description in expert terms
Provide a free-text explanation of the greenhouse in the expert’s own words.

### 6.3 Visual references
- Drawings available:
- Photos available:
- Layout available:
- CAD / engineering documentation available:
- Notes on missing visual material:

---

## 7. Structural system

### 7.1 Main structure
- Structural material:
- Main pillar profiles:
- Main span logic:
- Front pillar spacing:
- Internal pillar spacing (transverse):
- Internal pillar spacing (longitudinal):
- Arches / gothic shape description:
- Structural reinforcement logic:
- Bracing details:
- Connection types:
- Structural weak points known by experience:

### 7.2 Roof and load considerations
- Snow-load assumptions:
- Rain accumulation concerns:
- Roof weak points:
- Structural deformation concerns:
- Historical load incidents:
- Manual interventions used in adverse weather:
- Conditions under which structure becomes operationally unsafe:

### 7.3 Gutters and drainage collection
- Gutter arrangement:
- Gutter materials:
- Gutter length logic:
- Main accumulation points:
- Downpipes:
- Downpipe diameter:
- Downpipe material:
- Underground drainage description:
- Known clogging or overload risks:
- Maintenance practices:

### 7.4 Structural dependencies relevant for Agro-DO
- Which structural limits can affect operation?
- Which weather conditions alter safe operating modes?
- Which assets depend on structural integrity?
- Which structural issues can trigger irrigation or climate decisions?

---

## 8. Sectorization and zoning

### 8.1 Physical zones
For each zone or sector, capture:
- Sector name / ID:
- Location:
- Approximate area:
- Crop type:
- Crop stage:
- Sensitivity level:
- Business value:
- Stress tolerance:
- Irrigation priority:
- Climate priority:
- Recovery priority:
- Special constraints:

### 8.2 Operational grouping
- Which sectors are managed together?
- Which sectors can be isolated?
- Which sectors share infrastructure?
- Which sectors must never be grouped during recovery?
- Which sectors are first to sacrifice under severe constraint?
- Which sectors must be protected first?

### 8.3 Sector priority policy
Describe explicitly:
- highest-priority sectors,
- medium-priority sectors,
- lowest-priority sectors,
- and the reasons behind those priorities.

---

## 9. Water system

### 9.1 Water sources
- Main water source:
- Secondary water source:
- Emergency water source:
- External tanker possibility:
- Water quality constraints:
- Source reliability:
- Seasonal variability:
- Legal or supply restrictions:

### 9.2 Storage
For each tank or reservoir:
- Asset ID:
- Asset name:
- Tank type:
- Capacity:
- Operating range:
- Minimum safe level:
- Critical level:
- Refill method:
- Refill speed:
- Sensor coverage:
- Known issues:
- Failure symptoms:
- Maintenance practices:

### 9.3 Pumping system
For each pump:
- Asset ID:
- Asset name:
- Pump function:
- Supported lines / sectors:
- Nominal performance:
- Backup availability:
- Failure consequences:
- Common degradation patterns:
- Known early warning signals:
- Manual override options:
- Maintenance notes:

### 9.4 Distribution network
- Main hydraulic lines:
- Secondary lines:
- Sector branch logic:
- Valve arrangement:
- Pressure dependencies:
- Flow dependencies:
- Single points of failure:
- Isolation points:
- Manual intervention points:

### 9.5 Irrigation logic
- Normal irrigation philosophy:
- Scheduling logic:
- Priority logic under scarcity:
- Rules for rationing:
- Rules for staged restart:
- Conditions for stopping irrigation:
- Conditions for resuming irrigation:
- Conditions for recovery via external supply:

### 9.6 Water-system operational thresholds
Capture real-world thresholds used by operators:
- minimum credible continuity level,
- interruption threshold,
- backup activation threshold,
- tanker request threshold,
- sector sacrifice threshold,
- recovery threshold.

---

## 10. Climate control system

### 10.1 Ventilation
For each ventilation subsystem:
- Asset ID:
- Asset name:
- Type:
- Physical location:
- Opening logic:
- Maximum opening range:
- Drive mechanism:
- Motor type:
- Control mode:
- Failure symptoms:
- Consequences of failure:
- Manual fallback:
- Seasonal constraints:

### 10.2 Heating
- Heating assets:
- Boiler description:
- Heat distribution logic:
- Zone dependencies:
- Backup logic:
- Critical operating modes:
- Failure consequences:
- Manual intervention procedures:

### 10.3 Cooling / humidity control
- Cooling assets:
- Fogging / humidity systems:
- Dehumidification logic if any:
- Environmental thresholds:
- Priority rules:
- Failure consequences:

### 10.4 Climate-policy rules
- Conditions that justify climate degradation:
- Conditions that justify interruption of automation:
- Conditions that justify human escalation:
- Conditions that create crop-disease risk:
- Interactions between climate and irrigation decisions:

---

## 11. Electrical and control infrastructure

### 11.1 Power architecture
- Main power source:
- Backup power source:
- Generator availability:
- UPS coverage:
- Critical loads:
- Non-critical loads:
- Load-shedding logic:
- Known power vulnerabilities:

### 11.2 Control architecture
- Main controller:
- Local controllers:
- PLCs:
- SCADA / HMI:
- Remote supervision:
- Connectivity dependencies:
- Network dependencies:
- Manual control alternatives:
- Known communication weak points:

### 11.3 Automation philosophy
- What is automated?
- What is semi-automatic?
- What is manual?
- What should be locked under alarm?
- What can be overridden manually?
- What kinds of mismatch between digital and physical state are common?

---

## 12. Sensors and observability

### 12.1 Sensor inventory
For each important sensor:
- Sensor ID:
- Sensor name:
- Measured variable:
- Asset / zone covered:
- Unit:
- Expected operating range:
- Warning range:
- Critical range:
- Trust level:
- Common drift patterns:
- Failure symptoms:
- Flatline risk:
- Calibration method:
- Maintenance frequency:

### 12.2 Observability gaps
- Which assets lack sensors?
- Which states are inferred instead of observed?
- Which sensors are known to be unreliable?
- Which failures are often detected late?
- Which blind spots matter most for decision quality?

### 12.3 Sensor-trust policy
- When should data be trusted?
- When should it be doubted?
- What combinations of signals indicate sensor failure?
- What signals justify human escalation due to uncertainty?

---

## 13. Manual operations and operator practices

### 13.1 Routine manual actions
- What operators do regularly:
- What is done manually in abnormal conditions:
- What manual actions are safe:
- What manual actions are risky:
- What manual actions are often forgotten or delayed:

### 13.2 Emergency procedures
- Manual emergency stop logic:
- Manual recovery logic:
- Manual connection of tanker or emergency supply:
- Staged restart procedure:
- Forced ventilation / forced irrigation steps:
- Priority decisions usually taken by experienced operators:

### 13.3 Human bottlenecks
- Actions that require specific personnel:
- Actions that require multiple people:
- Actions that take too long:
- Actions that are easy to do wrong:
- Operational delays caused by human intervention:

---

## 14. Failure modes and known problematic situations

### 14.1 Major failure families
Describe the main failure families known in practice:
- water depletion,
- pump degradation,
- valve failure,
- hydraulic instability,
- sensor failure,
- communication loss,
- climate-control failure,
- structural weather risk,
- power loss,
- manual override mismatch,
- any other critical family.

### 14.2 For each relevant failure mode, capture:
- Failure mode name:
- Typical causes:
- Early signals:
- Late signals:
- Immediate consequences:
- Sector impact:
- Business impact:
- Recovery options:
- Common operator mistake:
- Whether Agro-DO should escalate, adjust, stop, or switch if this happens:

### 14.3 Historical examples
If available, describe real or representative incidents:
- What happened?
- What signals appeared first?
- What decision was taken?
- Was it the right decision?
- What would have improved the outcome?

---

## 15. Recovery paths and backup strategies

### 15.1 Internal recovery paths
- Backup pumps:
- Backup lines:
- Backup sectors:
- Degraded operating modes:
- Rationing logic:
- Selective continuity logic:
- Conditions for activating internal backup paths:

### 15.2 External recovery paths
- Tanker supply:
- Neighboring reserve sharing:
- Emergency external refill:
- Temporary manual supply:
- External contractors:
- Activation conditions:
- Typical arrival times:
- Reliability level:
- Operational burden:
- Cost burden:
- Connection complexity:

### 15.3 Recovery credibility factors
- What makes a recovery path strong?
- What makes it weak?
- What makes it usable but constrained?
- What makes it too weak to rely on?

### 15.4 Recovery prioritization policy
- Which sector is first to recover?
- Which sector can wait?
- Which continuity mode is acceptable under constrained recovery?
- When should recovery be abandoned and interruption accepted?

---

## 16. Decision rules already used by experts

### 16.1 Explicit rules
List any decision rules already used in practice.

Examples:
- If tank level falls below X and no refill is confirmed, do Y.
- If pressure behaves like X and flow behaves like Y, treat the line as unstable.
- If sector A and sector B compete for continuity, protect A first.
- If tanker arrival is delayed beyond X hours, do not continue irrigation.

### 16.2 Tacit rules
Capture practical rules the expert uses but may not normally write down.

Examples:
- “When this pattern appears, we do not trust the sensor.”
- “This valve usually fails after this symptom.”
- “That backup is only useful on paper, not in real life.”
- “This recovery path works only if the operator is already on site.”

---

## 17. Runtime state fields needed later by Agro-DO

Identify the variables that should exist in the future runtime context model.

Examples:
- tank level,
- line pressure,
- flow stability,
- sector moisture,
- actuator status,
- controller mode,
- communication status,
- sensor trust,
- manual override state,
- external supply status,
- sector priority state,
- recovery path availability.

For each variable:
- Variable name:
- Meaning:
- Source:
- Update frequency:
- Reliability:
- Importance for decisions:

---

## 18. What Agro-DO would need to reason correctly

Use this section to answer directly:

### 18.1 In difficult cases, what must Agro-DO know?
- Physical dependencies:
- Priority logic:
- Recovery options:
- Operational constraints:
- Seasonal constraints:
- Human bottlenecks:
- Sensor trust logic:
- Safety boundaries:

### 18.2 What mistakes would Agro-DO make if this information were missing?
Describe likely failure modes of the orchestrator if context is absent or too vague.

---

## 19. Missing information and follow-up questions

### 19.1 Missing knowledge
- What is still unknown?
- What needs confirmation?
- What needs measurement?
- What needs drawings or photos?

### 19.2 Follow-up questions for the expert
List the next questions to clarify in future sessions.

---

## 20. Final expert comments

Use this section for anything that does not fit neatly into the previous structure but should not be lost.

Examples:
- “This detail seems minor, but in practice it changes everything.”
- “The manuals say one thing, but operators do another.”
- “This subsystem is technically present but operationally useless.”
- “This recovery path exists only under certain people or timing conditions.”

---

## 21. Editorial note for future conversion

When this template is sufficiently filled, its contents should later be translated into:

- a structured greenhouse blueprint,
- a normalized asset and topology model,
- a runtime state model,
- and a decision-case generation layer for Agro-DO.

Do not simplify this document too early.  
Only simplify after observing what Agro-DO really needs in complex cases.
