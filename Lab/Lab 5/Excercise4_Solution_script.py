import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
linreg = LinearRegression()

houseData = pd.read_csv('train.csv')
houseGrLivArea = pd.DataFrame(houseData['GrLivArea'])
houseSalePrice = pd.DataFrame(houseData['SalePrice'])

sb.jointplot(data = houseData, x = "GrLivArea", y = "SalePrice", height = 12)
plt.show()

houseGrLivArea_train = pd.DataFrame(houseGrLivArea[:1100])
houseSalePrice_train = pd.DataFrame(houseSalePrice[:1100])
houseGrLivArea_test = pd.DataFrame(houseGrLivArea[-360:])
houseSalePrice_test = pd.DataFrame(houseSalePrice[-360:])
print('Train Set: ', houseGrLivArea_train.shape, houseSalePrice_train.shape)
print('Test Set: ', houseGrLivArea_test.shape, houseSalePrice_test.shape)

linreg.fit(houseGrLivArea_train,houseSalePrice_train)
print('Coefficients \t: a = ', linreg.coef_)

regline_x = houseGrLivArea_train
regline_y = linreg.intercept_ + linreg.coef_ * houseGrLivArea_train
f = plt.figure(figsize = (16,8))
plt.scatter(houseGrLivArea_train,houseSalePrice_train)
plt.plot(regline_x.to_numpy(), regline_y.to_numpy(), 'r-',linewidth = 3)
plt.show()
