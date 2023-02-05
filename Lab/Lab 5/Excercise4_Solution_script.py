import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
linreg = LinearRegression()

import sys

houseData = pd.read_csv('train.csv')
houseGrLivArea = pd.DataFrame(houseData['GrLivArea'])
houseSalePrice = pd.DataFrame(houseData['SalePrice'])
houseLotArea = pd.DataFrame(houseData['LotArea'])
houseGarageArea = pd.DataFrame(houseData['GarageArea'])
houseTotalBsmtSF = pd.DataFrame(houseData['TotalBsmtSF'])

sb.jointplot(data = houseData, x = "GrLivArea", y = "SalePrice", height = 12)
plt.show()
sb.jointplot(data = houseData, x = "LotArea", y = "SalePrice", height = 12)
plt.show()
sb.jointplot(data = houseData, x = "GarageArea", y = "SalePrice", height = 12)
plt.show()
sb.jointplot(data = houseData, x = "TotalBsmtSF", y = "SalePrice", height = 12)
plt.show()

houseSalePrice_train = pd.DataFrame(houseSalePrice[:1100])
houseSalePrice_test = pd.DataFrame(houseSalePrice[-360:])
#vs
houseGrLivArea_train = pd.DataFrame(houseGrLivArea[:1100])
houseGrLivArea_test = pd.DataFrame(houseGrLivArea[-360:])

houseLotArea_train = pd.DataFrame(houseLotArea[:1100])
houseLotArea_test = pd.DataFrame(houseLotArea[-360:])

houseGarageArea_train = pd.DataFrame(houseGarageArea[:1100])
houseGarageArea_test = pd.DataFrame(houseGarageArea[-360:])

houseTotalBsmtSF_train = pd.DataFrame(houseTotalBsmtSF[:1100])
houseTotalBsmtSF_test = pd.DataFrame(houseTotalBsmtSF[-360:])

def linregplot(x_Train, salePrice_Train, x_Test, salePrice_Test):

    linreg.fit(x_Train,salePrice_Train)
    print('Coefficients \t: a = ', linreg.coef_)

    regline_x = x_Train
    regline_y = linreg.intercept_ + linreg.coef_ * x_Train

    f = plt.figure(figsize = (16,9))
    plt.scatter(x_Train,salePrice_Train)
    plt.plot(regline_x.to_numpy(), regline_y.to_numpy(), 'r-',linewidth = 3)
    plt.show()

    SalePrice_prediction = linreg.predict(x_Test)
    f = plt.figure(figsize = (16,9))
    plt.scatter(x_Test, salePrice_Test)
    plt.scatter(x_Test, SalePrice_prediction, color = "r")
    plt.show()


    # Explained Variance (R^2)
    print("Explained Variance (R^2) \t:", linreg.score(x_Train, salePrice_Train))
    print("Explained Variance (R^2) \t:", linreg.score(x_Test, salePrice_Test))
    
linregplot(houseGrLivArea_train,houseSalePrice_train,houseGrLivArea_test,houseSalePrice_test)
linregplot(houseLotArea_train,houseSalePrice_train,houseLotArea_test,houseSalePrice_test)
linregplot(houseGarageArea_train,houseSalePrice_train,houseGarageArea_test,houseSalePrice_test)
linregplot(houseTotalBsmtSF_train,houseSalePrice_train,houseTotalBsmtSF_test,houseSalePrice_test)

