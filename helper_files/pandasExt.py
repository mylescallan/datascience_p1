from pandas.core.base import PandasObject
import pandas as pd
import numpy as np

def myDescribe(df,interval=0.1):
    """Do my stuff"""
    return df.describe(np.arange(0,1+interval,interval))
    
def myBins(df,var):
    describe = df[var].myDescribe()
    intervals = describe.index[~describe.index.isin(['count', 'mean', 'std', 'min','max'])]
    bins = [describe.loc[intervals[ind]] for ind in range(len(intervals)) if  describe.loc[intervals[ind]] != describe.loc[intervals[ind-1]]]
    bins = [round(x,2) for x in bins]
    labels = [intervals[ind] for ind in range(len(intervals)) if  describe.loc[intervals[ind]] != describe.loc[intervals[ind-1]]]
    labels[-1] = "100%"
    print(bins, labels)
    labels = [f"{str(bins[ind])} ({labels[ind].replace('%','th')})" for ind in range(len(labels))]
    return (bins,labels)
    
def myCut(df,var):
    bins, labels = myBins(df,var)
    var_name = f"{var.replace('_',' ')} Percentiles".title()
    df[var_name] = pd.cut(df[var],
                          bins,
                          labels=labels[1:],
                          include_lowest=True)
    return var_name
    
PandasObject.myDescribe = myDescribe
PandasObject.myBins = myBins
PandasObject.myCut = myCut