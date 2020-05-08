import numpy as np
import numpy.linalg as la
import collections


def decision_rank(decision_matrix, damping_factor) :
    n = decision_matrix.shape[0]

    M = damping_factor * decision_matrix + (1 - damping_factor) / n * np.ones([n, n])
    r = 100 * np.ones(n) / n
    lastR = r
    r = M @ r

    while la.norm(lastR - r) > 0.01 :
        lastR = r
        r = M @ r
    return r


def check_if_tie(ranking: list) -> bool:
    if len(ranking) == len(set(ranking)):
        return False
    else:
        return True


def get_tie_indices(ranking: list):
    tie_values = [item for item, count in collections.Counter(ranking).items() if count > 1]
    tie_indices = [i for i, x in enumerate(ranking) if x == tie_values[0]]

    return tie_indices[0], tie_indices[1]


def return_ranked_list(user_list: list, weights: list) -> list:
    final = []
    sorted_idx = sorted(range(len(weights)), key=lambda k: weights[k], reverse=True)

    for i in sorted_idx:
        final.append(user_list[i])

    return final
