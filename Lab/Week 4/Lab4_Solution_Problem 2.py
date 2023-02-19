import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
sb.set()

houseData = pd.read_csv('train.csv')
houseCatData = pd.DataFrame(houseData[['MSSubClass', 'Neighborhood', 'BldgType', 'OverallQual']])
print(houseCatData.astype('category').dtypes)
#convert all variables to 'category'

sb.catplot(y = "MSSubClass", data = houseCatData, kind = "count",height = 8)
sb.catplot(y = "Neighborhood", data = houseCatData, kind = "count",height = 8)
sb.catplot(y = "BldgType", data = houseCatData, kind = "count",height = 8)
sb.catplot(y = "OverallQual", data = houseCatData, kind = "count",height = 8)
plt.show()
#catplot of all Category Variables

f ,axes = plt.subplots(1,3,figsize=(20, 20))
sb.heatmap(houseCatData.groupby(['MSSubClass', 'OverallQual']).size().unstack(), 
           linewidths = 8, annot = False,cmap = "BuGn",ax = axes[0])
sb.heatmap(houseCatData.groupby(['Neighborhood', 'OverallQual']).size().unstack(), 
           linewidths = 8,annot = False, cmap = "BuGn",ax = axes[1])
sb.heatmap(houseCatData.groupby(['BldgType', 'OverallQual']).size().unstack(), 
           linewidths = 8, annot = False, cmap = "BuGn",ax = axes[2])
plt.show()
#relationship between 'OverallQual' and the rest of variables using Bi-variate heatmaps

f, axes = plt.subplots(4,1,figsize=(20,20))
sb.boxplot(x = houseData['SalePrice'], y= houseCatData['MSSubClass'],orient= 'h',ax = axes[0,])
sb.boxplot(x = houseData['SalePrice'], y= houseCatData['Neighborhood'],orient= 'h',ax = axes[1,])
sb.boxplot(x = houseData['SalePrice'], y= houseCatData['BldgType'],orient= 'h',ax = axes[2,])
sb.boxplot(x = houseData['SalePrice'], y= houseCatData['OverallQual'],orient= 'h',ax = axes[3,])
plt.show()
#relationship between Category Variables and 'SalePrice' using boxplot


