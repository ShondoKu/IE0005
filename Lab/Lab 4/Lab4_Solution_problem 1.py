import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
sb.set()

houseData = pd.read_csv('train.csv')
houseNumData = pd.DataFrame(houseData[['LotArea', 'GrLivArea', 'TotalBsmtSF', 'GarageArea', 'SalePrice']])
print(houseNumData)

f, axes = plt.subplots(5, 3, figsize=(18, 24))

count = 0
for var in houseNumData:
    sb.boxplot(data = houseNumData[var], orient = "h", ax = axes[count,0])
    sb.histplot(data = houseNumData[var], ax = axes[count,1])
    sb.violinplot(data = houseNumData[var], orient = "h", ax = axes[count,2])
    count += 1
plt.show()
#lotArea has maximum outliner



f = plt.figure(figsize=(12, 12))
sb.heatmap(houseNumData.corr(), vmin = -1, vmax = 1, annot = True, fmt = ".2f")
plt.show()
#heatmap of correlation of variables


sb.jointplot(data = houseNumData, x = "LotArea", y = "SalePrice", height = 12)
plt.show() 

sb.jointplot(data = houseNumData, x = "GrLivArea", y = "SalePrice", height = 12)
plt.show()

sb.jointplot(data = houseNumData, x = "TotalBsmtSF", y = "SalePrice", height = 12)
plt.show()

sb.jointplot(data = houseNumData, x = "GarageArea", y = "SalePrice", height = 12)
plt.show()
#mutual jointplot with 'SalePrice'

sb.pairplot(data = houseNumData)
plt.show()
#plot of all variables against each other

