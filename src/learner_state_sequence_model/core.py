from collections import defaultdict
from math import log2


def transition_matrix(states):
    """Estimate observed first order transition probabilities."""
    counts = defaultdict(lambda: defaultdict(int))
    totals = defaultdict(int)
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


def transition_entropy(states):
    """Return Shannon entropy for outgoing transitions from each observed state."""
    matrix = transition_matrix(states)
    return {
        state: -sum(probability * log2(probability) for probability in probabilities.values() if probability > 0)
        for state, probabilities in matrix.items()
    }


def persistence(states):
    """Return the fraction of adjacent observations that remain in the same state."""
    if len(states) < 2:
        return 1.0
    return sum(a == b for a, b in zip(states, states[1:])) / (len(states) - 1)
