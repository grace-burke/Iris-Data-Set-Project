# Iris Data Set
# http://archive.ics.uci.edu/ml/datasets/Iris

# https://www.kaggle.com/ashokdavas/iris-data-analysis-pandas-numpy

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


with open("Output File.txt","w") as outputfile:
    with open('Data/IrisData.csv') as f:

        column_names = ['Sepal Length','Sepal Width','Petal Length','Petal Width','Class']
        Iris = pd.read_csv(f, header=None,names=column_names)
        # https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
    
    outputfile.write("All Iris Classes\n")
    outputfile.write(Iris.describe().round(decimals=2).to_string()+"\n\n")
    
    bin_values = np.arange(start=0, stop=8, step=0.2)
    Iris.plot(kind='hist',bins=bin_values, alpha=0.6, title = "Iris Dataset Analysis").set_xlabel("(cm)")
    # https://community.modeanalytics.com/python/tutorial/python-histograms-boxplots-and-distributions/
    

    def AnalyseIris(x):
        if x in ("Iris-setosa", "Iris-versicolor", "Iris-virginica"):
            outputfile.write(x[:4]+" "+x.replace(x[:5], '')+"\n")
            # https://stackoverflow.com/questions/11806559/removing-first-x-characters-from-string
            outputfile.write(Iris.loc[Iris['Class'] == x].describe().round(decimals=2).to_string()+"\n\n")
            # https://stackoverflow.com/questions/31756340/selecting-rows-from-a-dataframe-based-on-values-in-multiple-columns-in-pandas
        Iris.loc[Iris['Class'] == x].plot(kind='hist',bins=bin_values, alpha=0.6, title = x[:4]+" "+x.replace(x[:5], '')+" Analysis").set_xlabel("(cm)")


    AnalyseAgain = input("Would you like to analyse an individual iris class? y/n: ")

    
    while AnalyseAgain == "y":
        IrisType = 1
        while IrisType not in ("Iris-setosa", "Iris-versicolor", "Iris-virginica"):
            try:
                IrisType = input("Which class of iris would you like to analyse? (Iris-setosa/Iris-versicolor/Iris-virginica): ")
                AnalyseIris(IrisType)
            except:
                print("Error: Please enter iris class exactly as shown above.")
        AnalyseAgain = input("Would you like to analyse another iris class? y/n: ")
        
plt.show()    