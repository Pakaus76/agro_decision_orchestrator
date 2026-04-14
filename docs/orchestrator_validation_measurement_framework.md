# Orchestrator Validation Measurement Framework

## 1. Purpose

This document defines a formal framework to measure the performance of Agro Decision Orchestrator (Agro-DO) in a repeatable and auditable way.

The framework combines:

- objective indicators,
- subjective indicators,
- explicit calculation formulas,
- and explicit data sources.

Its purpose is to validate Agro-DO beyond personal opinion.

---

## 2. Scope

This framework should be applied to:

- controlled validation cases,
- simulated scenarios,
- baseline comparisons,
- expert review sessions,
- and future shadow-mode observations.

---

## 3. Data sources

Use the following source codes in all evaluations.

### DS-01. Scenario Registry
Source:
- validated case files
- scenario metadata
- scenario family labels
- expected policy mode

Typical files:
- `inputs/sample_cases/*.json`
- scenario inventory sheets

### DS-02. Agro-DO Output Log
Source:
- final Agro-DO recommendations
- priority
- action type
- confidence
- rationale
- implicated assets
- next checks

Typical files:
- governed output JSON
- runtime logs

### DS-03. Baseline Output Log
Source:
- outputs from baseline policies
- deterministic rules
- conservative stop policy
- heuristic policies

### DS-04. Expert Panel Score Sheets
Source:
- structured expert scoring forms
- case review notes
- accept / reject decisions

Recommended panel:
- domain expert
- technical expert
- agronomic or operational expert

### DS-05. Simulation Results
Source:
- simulated crop impact
- water use
- continuity preservation
- recovery time
- cost impact
- sector-level outcomes

### DS-06. Hard Constraint Rulebook
Source:
- safety rules
- operational rules
- priority rules
- mandatory stop rules
- backup activation rules

### DS-07. Robustness Test Log
Source:
- repeated runs with controlled perturbations
- sensor-trust changes
- delay changes
- pressure or flow changes
- sector-priority changes

### DS-08. Confidence Log
Source:
- Agro-DO confidence labels
- final expert acceptance result
- final simulation result class

---

## 4. Subjective scoring scale

Use a 1 to 5 scale.

- 1 = unacceptable
- 2 = weak
- 3 = acceptable
- 4 = good
- 5 = very good

Formula:
`Subjective Score = Sum of evaluator scores / Number of evaluator scores`

Data source:
- DS-04

---

## 5. Objective indicators

## O-01. Hard Safety Violation Rate

Definition:
Percentage of cases where Agro-DO violates at least one non-negotiable rule.

Formula:
`Hard Safety Violation Rate (%) = (Cases with at least one hard-rule violation / Total evaluated cases) x 100`

Target direction:
Lower is better.

Data source:
- DS-02
- DS-06

---

## O-02. Policy Mode Accuracy

Definition:
Percentage of cases where Agro-DO selects the expected policy mode.

Valid modes:
- `switch_to_backup`
- `adjust_operation`
- `stop_and_review`
- `escalate_to_human`

Formula:
`Policy Mode Accuracy (%) = (Cases with correct policy mode / Total evaluated cases) x 100`

Target direction:
Higher is better.

Data source:
- DS-01
- DS-02

---

## O-03. Expert Acceptance Rate

Definition:
Percentage of cases where the expert panel rates the recommendation as at least acceptable.

Acceptance threshold:
Average panel score >= 3.0

Formula:
`Expert Acceptance Rate (%) = (Cases with panel average score >= 3.0 / Total evaluated cases) x 100`

Target direction:
Higher is better.

Data source:
- DS-04

---

## O-04. Expert Preference Rate versus Baseline

Definition:
Percentage of comparison cases where the expert panel rates Agro-DO higher than the baseline.

Formula:
`Expert Preference Rate (%) = (Cases where Agro-DO score > Baseline score / Total comparison cases) x 100`

Target direction:
Higher is better.

Data source:
- DS-03
- DS-04

---

## O-05. Dominated Decision Rate

Definition:
Percentage of cases where Agro-DO produces a decision that is clearly worse than another available evaluated option.

A decision is dominated when another option is at least equal on all critical dimensions and strictly better on at least one critical dimension.

Formula:
`Dominated Decision Rate (%) = (Dominated Agro-DO decisions / Total evaluated cases) x 100`

Target direction:
Lower is better.

Data source:
- DS-02
- DS-03
- DS-05
- DS-04

---

## O-06. Baseline Improvement Rate

Definition:
Percentage of cases where Agro-DO performs better than the baseline on simulated outcome score.

Formula:
`Baseline Improvement Rate (%) = (Cases where Agro-DO Outcome Score > Baseline Outcome Score / Total comparison cases) x 100`

Target direction:
Higher is better.

Data source:
- DS-03
- DS-05

---

## O-07. Simulated Outcome Score

Definition:
Composite score used to compare decisions on operational outcome.

Recommended normalized components:
- continuity preservation score
- crop protection score
- water efficiency score
- recovery effectiveness score
- cost control score

Formula:
`Simulated Outcome Score = (0.30 x Continuity Score) + (0.30 x Crop Protection Score) + (0.15 x Water Efficiency Score) + (0.15 x Recovery Effectiveness Score) + (0.10 x Cost Control Score)`

All sub-scores must be normalized to a 0 to 100 scale.

Target direction:
Higher is better.

Data source:
- DS-05

---

## O-08. Resource Efficiency Index

Definition:
Efficiency of the decision in preserving useful outcome per unit of critical resource consumed.

Recommended first resource:
water

Formula:
`Resource Efficiency Index = Useful Outcome Score / Water Used`

Alternative normalized formula:
`Resource Efficiency Index = Normalized Useful Outcome Score / Normalized Resource Consumption`

Target direction:
Higher is better.

Data source:
- DS-05

---

## O-09. Recovery Path Use Accuracy

Definition:
Accuracy in deciding whether a backup or recovery path should be activated.

Formula:
`Recovery Path Use Accuracy (%) = (Cases where Agro-DO correctly activates or correctly rejects recovery path / Total recovery-related cases) x 100`

Target direction:
Higher is better.

Data source:
- DS-01
- DS-02
- DS-04

---

## O-10. Sector Prioritization Accuracy

Definition:
Accuracy in protecting, reducing, or sacrificing the correct sectors in constrained continuity scenarios.

Formula:
`Sector Prioritization Accuracy (%) = (Cases where observed sector treatment matches expected priority logic / Total prioritization cases) x 100`

Target direction:
Higher is better.

Data source:
- DS-01
- DS-02
- DS-04
- DS-05

---

## O-11. Robustness Stability Rate

Definition:
Percentage of non-material perturbation runs where Agro-DO keeps a stable recommendation.

Formula:
`Robustness Stability Rate (%) = (Stable decisions under non-material perturbations / Total non-material perturbation runs) x 100`

Target direction:
Higher is better.

Data source:
- DS-07

---

## O-12. Robustness Sensitivity Rate

Definition:
Percentage of material perturbation runs where Agro-DO changes the recommendation correctly.

Formula:
`Robustness Sensitivity Rate (%) = (Correctly changed decisions under material perturbations / Total material perturbation runs) x 100`

Target direction:
Higher is better.

Data source:
- DS-07
- DS-04

---

## O-13. Confidence Calibration Accuracy

Definition:
Degree to which Agro-DO confidence labels reflect actual decision quality.

Success rule:
A case is a success when it is accepted by experts and is not dominated.

Supporting formulas:
`High Confidence Success Rate (%) = (Successful high-confidence cases / Total high-confidence cases) x 100`

`Low Confidence Success Rate (%) = (Successful low-confidence cases / Total low-confidence cases) x 100`

Main formula:
`Confidence Calibration Accuracy = High Confidence Success Rate - Low Confidence Success Rate`

Target direction:
Higher is better, provided high-confidence success is strong.

Data source:
- DS-02
- DS-04
- DS-05
- DS-08

---

## 6. Subjective indicators

## S-01. Operational Feasibility Score

Definition:
Expert judgment of whether the recommendation can realistically be executed in the greenhouse context.

Formula:
`Operational Feasibility Score = Sum of evaluator scores / Number of evaluator scores`

Target direction:
Higher is better.

Data source:
- DS-04

---

## S-02. Agronomic Adequacy Score

Definition:
Expert judgment of whether the recommendation protects crop priorities correctly.

Formula:
`Agronomic Adequacy Score = Sum of evaluator scores / Number of evaluator scores`

Target direction:
Higher is better.

Data source:
- DS-04

---

## S-03. Business Adequacy Score

Definition:
Expert judgment of whether the recommendation makes sense from a continuity, loss, and value-preservation perspective.

Formula:
`Business Adequacy Score = Sum of evaluator scores / Number of evaluator scores`

Target direction:
Higher is better.

Data source:
- DS-04

---

## S-04. Safety Appropriateness Score

Definition:
Expert judgment of whether the recommendation is appropriately conservative or appropriately interventionist for the case.

Formula:
`Safety Appropriateness Score = Sum of evaluator scores / Number of evaluator scores`

Target direction:
Higher is better.

Data source:
- DS-04

---

## S-05. Recovery Logic Quality Score

Definition:
Expert judgment of whether the recommendation uses backup or recovery paths correctly.

Formula:
`Recovery Logic Quality Score = Sum of evaluator scores / Number of evaluator scores`

Target direction:
Higher is better.

Data source:
- DS-04

---

## S-06. Explanation Quality Score

Definition:
Expert judgment of whether the rationale is clear, relevant, and traceable.

Formula:
`Explanation Quality Score = Sum of evaluator scores / Number of evaluator scores`

Target direction:
Higher is better.

Data source:
- DS-04

---

## S-07. Operator Trust Score

Definition:
Expert or operator judgment of whether they would trust Agro-DO enough to use it as serious decision support in practice.

Formula:
`Operator Trust Score = Sum of evaluator scores / Number of evaluator scores`

Target direction:
Higher is better.

Data source:
- DS-04

---

## 7. Minimum case evaluation record

Each evaluated case should produce at least these fields:

1. case identifier
2. scenario family
3. expected policy mode
4. Agro-DO output
5. baseline output
6. hard-rule violation flag
7. simulation outcome summary
8. expert panel scores
9. acceptance result
10. dominance result
11. confidence label
12. recovery-path classification if applicable

Data source:
- DS-01
- DS-02
- DS-03
- DS-04
- DS-05
- DS-06
- DS-08

---

## 8. Minimum reporting pack

For each validation batch, report at minimum:

### Objective metrics
- Hard Safety Violation Rate
- Policy Mode Accuracy
- Expert Acceptance Rate
- Expert Preference Rate versus Baseline
- Dominated Decision Rate
- Baseline Improvement Rate
- Simulated Outcome Score
- Resource Efficiency Index
- Recovery Path Use Accuracy
- Sector Prioritization Accuracy
- Robustness Stability Rate
- Robustness Sensitivity Rate
- Confidence Calibration Accuracy

### Subjective metrics
- Operational Feasibility Score
- Agronomic Adequacy Score
- Business Adequacy Score
- Safety Appropriateness Score
- Recovery Logic Quality Score
- Explanation Quality Score
- Operator Trust Score

---

## 9. Recommended acceptance logic

Agro-DO should be considered strong enough for the current stage when all of the following are broadly true:

1. Hard Safety Violation Rate is near zero.
2. Policy Mode Accuracy is high across main families.
3. Expert Acceptance Rate is consistently high.
4. Dominated Decision Rate is low.
5. Agro-DO outperforms simple baselines in a meaningful share of cases.
6. Recovery Path Use Accuracy is high in recovery-related cases.
7. Sector Prioritization Accuracy is high in constrained continuity cases.
8. Subjective scores are at least acceptable, and preferably good, across the main dimensions.
9. Confidence labels show at least basic calibration.

---

## 10. Final note

This framework is designed to move Agro-DO validation from informal opinion to structured evidence.

The system does not need to prove perfect universal correctness.

It needs to prove that it is:

- safe,
- coherent,
- more useful than simple baselines,
- aligned with expert judgment,
- and robust enough to justify continued development.
