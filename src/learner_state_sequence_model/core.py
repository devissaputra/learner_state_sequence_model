# Calculation reading guide: ../CALCULATIONS.md (repository root).
# P(j|i) = count(i→j)/sum_j count(i→j); persistence = self-transitions/(n-1).
# A terminal state with no outgoing observation has no estimated transition row. Fewer than two observations make persistence undefined. These are descriptive first-order frequencies, not a trained sequence predictor.

from collections import defaultdict
from collections.abc import Hashable, Sequence
from math import log2


def transition_matrix(
    states: Sequence[Hashable],
) -> dict[Hashable, dict[Hashable, float]]:
    """Estimate observed first-order transition probabilities."""
    counts: dict[Hashable, dict[Hashable, int]] = defaultdict(lambda: defaultdict(int))
    totals: dict[Hashable, int] = defaultdict(int)

    for current, next_state in zip(states, states[1:]):
        counts[current][next_state] += 1
        totals[current] += 1

    return {
        current: {
            next_state: count / totals[current]
            for next_state, count in destinations.items()
        }
        for current, destinations in counts.items()
    }


def transition_entropy(states: Sequence[Hashable]) -> dict[Hashable, float]:
    """Return Shannon entropy for outgoing transitions from each observed state."""
    matrix = transition_matrix(states)
    return {
        state: -sum(
            probability * log2(probability)
            for probability in probabilities.values()
            if probability > 0
        )
        for state, probabilities in matrix.items()
    }


def persistence(states: Sequence[Hashable]) -> float | None:
    """Return the observed self-transition rate, or None when it is not estimable."""
    if len(states) < 2:
        return None
    return sum(a == b for a, b in zip(states, states[1:])) / (len(states) - 1)


def sequence_summary(states: Sequence[Hashable]) -> dict[str, object]:
    """Return a compact descriptive summary for one observed state sequence."""
    return {
        "observations": len(states),
        "unique_states": len(set(states)),
        "transitions": max(len(states) - 1, 0),
        "transition_matrix": transition_matrix(states),
        "transition_entropy": transition_entropy(states),
        "persistence": persistence(states),
    }
