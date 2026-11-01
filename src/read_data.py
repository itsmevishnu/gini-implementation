from __future__ import annotations
import pandas as pd
import numpy as np

from .helpers.helpers import check_csv

def read_file(file_path: str) -> list:
    if check_csv(file_path):
        df = pd.read_csv(file_path)
        if 'income' not in df.columns:
            raise Exception('No income column available, Invalid data')
        income_data = np.array(df["income"])

    return income_data
