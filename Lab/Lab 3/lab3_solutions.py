import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
sb.set()


#a)
trainData = pd.read_csv('house-prices-advanced-regression-techniques/train.csv')

#b)
'''print(trainData.head())
print("Data type : ", type(trainData))
print(trainData.dtypes)'''

#c)

#print(trainData.dtypes['Street'])
dictData = dict()
for x in trainData.columns:
    if trainData.dtypes[x] == "int64":
        dictData[x] = trainData[x]
int64Data = pd.DataFrame(dictData)
print(int64Data.dtypes)

#d)
y = int64Data.drop(['MSSubClass'],axis = 1,inplace = True)
print(int64Data)
print("Summary Statistics of SalePrice is :\n\n",int64Data['SalePrice'].describe())
'''f = plt.figure(figsize=(24,4))
sb.boxplot(data= int64Data['SalePrice'], orient = "h")
plt.show()

f = plt.figure(figsize=(16, 8))
sb.histplot(data = int64Data['SalePrice'])
plt.show()

sb.kdeplot(data = int64Data['SalePrice']) 
plt.show()

f = plt.figure(figsize=(24,4))
sb.boxplot(data= int64Data['LotArea'], orient = "h")
plt.show()

f = plt.figure(figsize=(16, 8))
sb.histplot(data = int64Data['LotArea'])
plt.show()

sb.kdeplot(data = int64Data['LotArea']) 
plt.show()

sb.jointplot(data = int64Data, x = "LotArea", y = "SalePrice", height = 12)
plt.show()'''
jointData = pd.concat([int64Data["LotArea"],int64Data["SalePrice"]],axis = 1).reindex(int64Data["LotArea"].index)
print(jointData.corr())
