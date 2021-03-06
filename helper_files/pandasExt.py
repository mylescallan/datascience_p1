from pandas.core.base import PandasObject
import pandas as pd
import numpy as np

def myDescribe(df,interval=0.1):
    """Do my stuff"""
    return df.describe(np.arange(0,1+interval,interval))

PandasObject.myDescribe = myDescribe