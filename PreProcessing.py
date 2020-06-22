import numpy as np
from sklearn.preprocessing import StandardScaler


def fill_numeric_nan(data):
    """ Fills NaN values in the given data with their column mean value"""

    for var in data.select_dtypes(include=np.number).columns:
        data[var] = data[var].fillna(np.mean(data[var]))
    return data


def standardization(data):
    """ Normalize all of the values in the given data to their standard value """

    numeric_cols = data.select_dtypes(include=np.number).columns
    data[numeric_cols] = StandardScaler().fit_transform(data[numeric_cols])
    return data


def group_by(data, col_title):
    """ Collect all of the records with the same value in col_title column to the same record,
        calculating the mean value for all values gathered together"""

    return data.groupby(by=[col_title], as_index=False).mean()


def pre_processing(data, group_by_col):
    """ Pre process the data in the data file in filename path and prepare it for clustering"""

    data = fill_numeric_nan(data)
    data = standardization(data)
    return group_by(data, group_by_col)

