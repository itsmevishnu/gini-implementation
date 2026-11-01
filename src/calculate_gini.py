from __future__ import annotations
import numpy as np

np.seterr(divide='ignore', invalid='ignore')

def calculate_gini(data: list) -> float:
    n = len(data)
    
    if n == 0:
        return 0.0

    if n == 1:
        return 1.0
    
    mean_data =  np.mean(data)

    if mean_data == 0:
        return 0.0

    sorted_data = sorted(data)

    sum = 0
    for i in range(n):
        for j in range(n):
            sum += np.abs(sorted_data[i] -  sorted_data[j])
    gini = np.round(sum / (2 * n * n * mean_data), 2)

    return gini