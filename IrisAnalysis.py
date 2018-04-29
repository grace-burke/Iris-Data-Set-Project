# Grace Burke
# 29/04/2018

# Iris Data Set
# http://archive.ics.uci.edu/ml/datasets/Iris

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Allows analysis output to be printed into new text file
with open("Output File.txt","w") as outputfile:
# http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
    
    # Opens data file to read data
    with open('Data/IrisData.csv') as f:

        # Reads data from csv file as dataframe using pandas library, giving each column a title
        column_names = ['Sepal Length','Sepal Width','Petal Length','Petal Width','Class']
        Iris = pd.read_csv(f, header=None,names=column_names)
    
    outputfile.write("All Iris Classes\n")
    # Produces a summary of each column of the data and writes it as a string to the output text file
    outputfile.write(Iris.describe().round(decimals=2).to_string()+"\n\n")
    
    # Sets up the bin values and steps for a histogram of the data using numpy library
    bin_values = np.arange(start=0, stop=8, step=0.2)
    # Plots the data as a histogram
    Iris.plot(kind='hist',bins=bin_values, alpha=0.6, title = "Iris Dataset Analysis").set_xlabel("(cm)")
    # https://community.modeanalytics.com/python/tutorial/python-histograms-boxplots-and-distributions/
    

    # Function which takes iris class as input and produces summary of each column of data and histogram for that iris class only
    def AnalyseIris(x):
        # Writes iris class to output text file removing the dash between words
        outputfile.write(x[:4]+" "+x.replace(x[:5], '')+"\n")
        # https://stackoverflow.com/questions/11806559/removing-first-x-characters-from-string
        # Filters dataframe by iris class, writes summary of data to output text file as before
        outputfile.write(Iris.loc[Iris['Class'] == x].describe().round(decimals=2).to_string()+"\n\n")
        # https://stackoverflow.com/questions/31756340/selecting-rows-from-a-dataframe-based-on-values-in-multiple-columns-in-pandas
        # Plots filtered data as histogram
        Iris.loc[Iris['Class'] == x].plot(kind='hist',bins=bin_values, alpha=0.6, title = x[:4]+" "+x.replace(x[:5], '')+" Analysis").set_xlabel("(cm)")

    # This variable accepts user input which will then determine whether while loop below is run
    AnalyseAgain = input("Would you like to analyse an individual iris class? y/n: ") 
    # When the user has selected yes, while loop runs to analyse data filtered by iris class nominated by user
    
    while AnalyseAgain == "y":
        # Sets initial value of IrisType to ensure that while loop below will run at least once
        IrisType = 1
        # Exception to catch user input in incorrect format and prompt the user to try again and enter the correct input
        while IrisType not in ("Iris-setosa", "Iris-versicolor", "Iris-virginica"):
            try:
                # Prompts user to input iris class for analysis
                IrisType = input("Which class of iris would you like to analyse? (Iris-setosa/Iris-versicolor/Iris-virginica): ")
                # Creates an error if iris class entered by user does not match the iris classes in the data
                if IrisType not in ("Iris-setosa", "Iris-versicolor", "Iris-virginica"):
                    raise TypeError
            except TypeError:
                # If running AnalyseIris above produces a TypeError because the user has entered an iris type that does not match an iris type in the data, this gives the user an error message and the while loop will run again prompting the user to enter iris type again
                print("Error: Please enter iris class exactly as shown above.")
        # Runs analysis function with iris class provided by user
        AnalyseIris(IrisType)
        # This gives the user the option to run the while loop again to analyse another class of iris
        AnalyseAgain = input("Would you like to analyse another iris class? y/n: ")
        
# This uses the matplotlib.pyplot library to show each of the histograms produced above in individual windows       
plt.show()    