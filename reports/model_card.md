# Analytic system card

## System

Learner State Sequence Model

## Purpose

Descriptive sequence analytics for learner state transitions, entropy, and persistence.

## Current maturity

Working research prototype. The bundled example checks the software path with synthetic inputs. It does not establish validity for real learners, instructors, courses, or workplaces.

## Inputs

See `../data/README.md` for the current synthetic schema and the documentation expected before real data are connected.

## Outputs

The current code produces first order transition probabilities, per state transition entropy, and sequence persistence. These outputs are research signals and should be interpreted with the educational context that produced them.

## Evidence needed before real use

Check whether transition estimates are stable with enough observations and whether state definitions are reliable across raters or labeling methods. Predictive claims require a separate forecasting model and holdout design.

## Main limitation

The module assumes that state labels already exist and are meaningful. It does not infer states from raw learner behavior and it does not forecast the next state.

## Human oversight

A person must review any output before it can affect a learner, instructor, applicant, or employee.
