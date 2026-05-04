import numpy as np

def hr_probability(score):
    # logistic conversion
    return 1 / (1 + np.exp(-8 * (score - 0.5)))
