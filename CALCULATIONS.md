# Calculation guide

## Question and evidence

How often do observed learner states persist or change?

A supplied sequence of state labels, not inferred psychological states.

**Status:** SYNTHETIC / RULE-BASED PROTOTYPE | no educational validity claim.

## Design

Count adjacent transitions; normalize outgoing counts; calculate entropy and self-transition frequency.

## Calculation and interpretation

`P(j|i) = count(i→j)/sum_j count(i→j); persistence = self-transitions/(n-1).`

A terminal state with no outgoing observation has no estimated transition row. Fewer than two observations make persistence undefined. These are descriptive first-order frequencies, not a trained sequence predictor.

## Evidence table

Worked example — illustrative, not a measured research result. Full precision below is for traceability, not a claim of measurement precision.

| Quantity | Value | Unit / meaning | JSON path |
|---|---:|---|---|
| self-transition proportion | 0.3333333333333333 | unitless | `outputs.self-transition proportion` |
| work transition entropy (bits) | 1.0 | unitless | `outputs.work transition entropy (bits)` |

Source: [results/review_examples.json](results/review_examples.json). Values resolve directly from this file when figures are regenerated.

This repository summarizes supplied learner-state sequences through transition probabilities, outgoing-state entropy, and persistence. Counts are normalized only where transitions are observed, and insufficient sequences return an undefined persistence value rather than a fabricated estimate. It is a descriptive baseline for sequence analysis; the labels must be justified separately and should not be treated as inferred mental states.

## Verification performed in this review

7 existing unittest checks passed. The bundled demonstration executed successfully in this review.

The figure-generation check verifies agreement between the selected source values and SVGs. It does not validate the raw dataset, fitted model, identification assumptions, or external generalization.

```bash
python scripts/build_review_figures.py
python scripts/build_review_figures.py --check
```

For the explicitly illustrative example:

```bash
python scripts/review_examples.py
```

## Implementation map

Follow these functions to inspect each transformation. Validation helpers and private functions remain visible in the linked modules.

| Function | Purpose / documented behavior |
|---|---|
| [`transition_matrix`](src/learner_state_sequence_model/core.py#L10) | Estimate observed first-order transition probabilities. |
| [`transition_entropy`](src/learner_state_sequence_model/core.py#L30) | Return Shannon entropy for outgoing transitions from each observed state. |
| [`persistence`](src/learner_state_sequence_model/core.py#L43) | Return the observed self-transition rate, or None when it is not estimable. |
| [`sequence_summary`](src/learner_state_sequence_model/core.py#L50) | Return a compact descriptive summary for one observed state sequence. |

## What remains before a stronger research claim

A terminal state with no outgoing observation has no estimated transition row. Fewer than two observations make persistence undefined. These are descriptive first-order frequencies, not a trained sequence predictor. A successful software test is not validation of a scientific construct. New experiments should state their split unit, comparator, outcome, uncertainty procedure and failure criteria before examining final test results.
