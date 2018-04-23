# Iris Data Set
# http://archive.ics.uci.edu/ml/datasets/Iris

# https://www.kaggle.com/ashokdavas/iris-data-analysis-pandas-numpy

import pandas as pd
import numpy as np

with open('Data/IrisData.csv') as f:

    column_names = ['Sepal Length','Sepal Width','Petal Length','Petal Width','Class']
    Iris = pd.read_csv(f, header=None,names=column_names)
    # https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
    Iris.index = np.arange(1,len(Iris)+1)
    # https://stackoverflow.com/questions/32249960/in-python-pandas-start-row-index-from-1-instead-of-zero-without-creating-additi
    # print(Iris)

    OverallStats = []
    for col in range(4):
        OverallStats.append([Iris.iloc[:,col].max(),Iris.iloc[:,col].min(),Iris.iloc[:,col].mean(),Iris.iloc[:,col].std()])
        # https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python  
    OverallStatsDF = pd.DataFrame(OverallStats)
    OverallStatsDF.columns = ['Max','Min','Mean','Standard Deviation']
    OverallStatsDF = OverallStatsDF.rename(index={0:'Sepal Length', 1:'Sepal Width', 2:'Petal Length', 3:'Petal Width'})
    # https://stackoverflow.com/questions/42142756/how-can-i-change-a-specific-row-label-in-a-pandas-dataframe
    print(OverallStatsDF)
