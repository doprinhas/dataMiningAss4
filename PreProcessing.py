import numpy as np
from sklearn.preprocessing import StandardScaler


def fill_numeric_nan(data):
    for var in data.select_dtypes(include=np.number).columns:
        data[var] = data[var].fillna(np.mean(data[var]))
    return data


def standardization(data):
    numeric_cols = data.select_dtypes(include=np.number).columns
    data[numeric_cols] = StandardScaler().fit_transform(data[numeric_cols])
    return data


def group_by(data, col_title):
    return data.groupby(by=[col_title], as_index=False).mean()


def pre_processing(data, group_by_col):
    data = fill_numeric_nan(data)
    data = standardization(data)
    return group_by(data, group_by_col)

