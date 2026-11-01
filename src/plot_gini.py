from __future__ import annotations
import numpy as np
import matplotlib.pyplot as plt


def calculate_cum_income_percentage(data: list) -> list:
    data_sorted = sorted(data)
    cum_income = np.cumsum(data_sorted)
    total = np.sum(data_sorted)

    cum_income_percentage = [np.round(item/total, 2) for item in cum_income]
    cum_income_percentage.insert(0,0) # added first value
    return cum_income_percentage

def calculate_perfect_equality(n: int) -> list:
    perfect_equality = np.linspace(0, 1, n)
    return perfect_equality

    
def plot_gini(data: list) -> None:
    cum_income_percentage = calculate_cum_income_percentage(data)
    perfect_equality = calculate_perfect_equality(len(cum_income_percentage))
    
    fig = plt.figure()
    plt.plot(cum_income_percentage)
    plt.plot(perfect_equality,  linestyle ='--')
    plt.title('Lorenze Curve', fontsize=14, fontweight='bold')
    plt.show()

