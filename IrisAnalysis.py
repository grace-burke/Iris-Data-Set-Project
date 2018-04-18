# Iris Data Set
# http://archive.ics.uci.edu/ml/datasets/Iris

with open("Data/IrisData.csv") as Iris:
    # The with keyword allows the data to be called from the address given, but only for the indented code. The data file is closed after this.

    for line in Iris:
        col1 = (line.split(',')[0])
        col2 = (line.split(',')[1])
        col3 = (line.split(',')[2])
        col4 = (line.split(',')[3])
        # For ease of reading, each of the columns is named separately.
        # For each line, the value up to the first comma is placed in col1, the value between the first and second comma is placed in col2, and so on.
        
        print('{:4s} {:4s} {:4s} {:4s}'\
        .format(col1,col2,col3,col4))
        # This formats the string values in col1 to col4 to contain a minimum of 4 characters.