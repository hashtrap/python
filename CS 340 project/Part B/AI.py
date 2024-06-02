import numpy as np
import pandas as pd
import sklearn as sk
# Create the sigmoid algorithm function
def sigmoid(x, derivative=False):
    if (derivative == True):
        return x * (1 - x)

    return 1 / (1 + np.exp(-x))

names=['variance','skewness','curtois','entropy','Class']

# Read dataset to pandas dataframe
irisdata = pd.read_csv('data_banknote_authentication.txt', names=names)

# Let us peek at the top of the data set, as imported in the irisdata dataframe
print("\nPrinting the first few lines of the data set:\n", irisdata.head() )

X = irisdata.iloc[:, 0:4]

# Assign data from first fifth columns to y variable
y = irisdata.select_dtypes(include=['int64'])

print("\n\nPrinting the first few lines of the 5th column (categories):\n", y.head() )


print ("\n\nPrinting the contents of the category column: ", y.Class.unique() )