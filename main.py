from __future__ import annotations
from src.read_data import read_file
from src.calculate_gini import calculate_gini
from src.plot_gini import plot_gini


FILE_PATH = r'data\data.csv'

if __name__ == "__main__":
    data = read_file(FILE_PATH)
    gini_score = calculate_gini(data)
    print(f"The Gini coeffient for the given data is  {gini_score}")
    plot_gini(data)
