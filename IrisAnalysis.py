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
    print(Iris[0:50].describe())
    print(Iris[50:100].describe())
    print(Iris[100:150].describe())
    print(Iris.groupby('Class').describe())
    
    bin_values = np.arange(start=0, stop=8, step=0.2)
    Iris.plot(kind='hist',bins=bin_values, alpha=0.6)
    Iris.groupby('Class').plot(kind='hist',bins=bin_values, alpha=0.6)
    # https://community.modeanalytics.com/python/tutorial/python-histograms-boxplots-and-distributions/


    plt.show()