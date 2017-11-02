"""Softmax."""

import numpy as np

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    return np.exp(x)/np.sum(np.exp(x), axis=0)


scores = [0.7, 0.0, 0.1, 0.2 ]

print(softmax(scores))
