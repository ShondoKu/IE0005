import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt 
from sklearn.neighbors import LocalOutlierFactor
sb.set()

#a)
houseData = pd.read_csv('train.csv')
#b)
x = pd.DataFrame(houseData[['GrLivArea','GarageArea']])
f, axes = plt.subplots(1,1, figsize = (16,8))
plt.scatter( x = "GrLivArea", y = 'GarageArea', data = x)
plt.show()
#c)
from sklearn.cluster import KMeans
#d)
guess_Num_clust = 2
kmeans = KMeans(n_clusters= guess_Num_clust)
kmeans.fit(x)

#e)
print("Features", "\tGrLivArea", "\tGarageArea")

for i, center in enumerate(kmeans.cluster_centers_):
    print("\nCluster", i , end = ":\t")
    for coord in center:
        print(round(coord,2),end="\t\t")


labels = kmeans.predict(x)
x_labeled = x.copy()
x_labeled["Cluster"] = pd.Categorical(labels)
sb.countplot(x = x_labeled["Cluster"])
plt.show()

f, axes = plt.subplots(1,1,figsize=(16,8))
plt.scatter(x = "GrLivArea", y = "GarageArea", c = "Cluster", cmap = "viridis", data = x_labeled)
plt.show()


num_neighbours = 5
cont_fractions = 0.025
lof = LocalOutlierFactor(n_neighbors = num_neighbours, contamination = cont_fractions)
lof.fit(x)

labels = lof.fit_predict(x)
x_labeled = x.copy()
x_labeled["Anomaly"] = pd.Categorical(labels)
sb.countplot(x = x_labeled["Anomaly"])
plt.show()

f, axes = plt.subplots(1,1,figsize=(16,8))
plt.scatter(x = "GrLivArea", y = "GarageArea", c = "Anomaly", cmap = 'viridis', data= x_labeled)
plt.show()