import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

df = pd.read_csv('2015-details.csv', index_col='Date')

df1 = df.dropna(thresh=3)  # keep the row at least 3 values
# deal with the date type

np.diff()