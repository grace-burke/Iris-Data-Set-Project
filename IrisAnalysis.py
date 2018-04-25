# Iris Data Set
# http://archive.ics.uci.edu/ml/datasets/Iris

# https://www.kaggle.com/ashokdavas/iris-data-analysis-pandas-numpy

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


with open('Data/IrisData.csv') as f:

    column_names = ['Sepal Length','Sepal Width','Petal Length','Petal Width','Class']
    Iris = pd.read_csv(f, header=None,names=column_names)
    # https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
    Iris.index = np.arange(1,len(Iris)+1)
    # https://stackoverflow.com/questions/32249960/in-python-pandas-start-row-index-from-1-instead-of-zero-without-creating-additi
    # print(Iris)
    
    print(Iris.describe())
    print(Iris.groupby('Class').describe())
    Iris.hist()
    Iris.groupby('Class').hist()
    plt.show()