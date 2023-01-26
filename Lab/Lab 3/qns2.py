# Basic Libraries
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt # we only need pyplot
sb.set() # set the default Seaborn style for graphics
intDict = dict()

# a)
csv_data = pd.read_csv('house-prices-advanced-regression-techniques/train.csv')
for x in csv_data.columns:
    if csv_data.dtypes[x] == np.int64:
        intDict[x] = csv_data[x]
intTable = pd.DataFrame(intDict)
#print("a) Summary Statistics of SalePrice : \n", newIntTable['SalePrice']. describe(), "\n")

# b)
#f = plt.figure(figsize=(24, 4))
#sb.boxplot(data = intTable, orient = "h")
f = plt.figure(figsize=(16, 8))
sb.histplot(data = intTable)
#plt.show()
# c) 
#print("c) Summary Statistics of LotArea : \n", newIntTable['LotArea']. describe(), "\n")