# -*- coding: utf-8 -*-


# Import convention
from sklearn.cluster import KMeans

import numpy as np
import matplotlib.pyplot as plt


"""
---------------------------
Load and plot the data (Task 1)
---------------------------
"""

# Load
dataRaw = np.loadtxt('exampleData.csv', delimiter=',', dtype='object')
header = dataRaw[0,:]
data = dataRaw[1:,:2]
data = np.vstack(data.astype(np.float32))

# Plot
fig, ax = plt.subplots()
ax.scatter(data[:,0],data[:,1])
ax.set_title('Rodent data')
ax.set_xlabel(header[0])
ax.set_ylabel(header[1])


"""
---------------------------
Execute K-Means clustering
---------------------------
"""

kmeans = KMeans(n_clusters=3, n_init=15)
kmeans.fit(data)
print("WCSS: ", kmeans.inertia_)
print("Iternations until converged: ", kmeans.n_iter_)
print("Final centroids: ")
print(kmeans.cluster_centers_)
print("Cluster assignments ")
print(kmeans.labels_)


"""
---------------------------
Visualize clustering (Task 2)
---------------------------
"""

fig, ax = plt.subplots()
idxs = np.unique(kmeans.labels_)

for i in idxs:
    #Points of cluster
    points = data[kmeans.labels_==i,:]
    #Plot points
    plt.scatter(points[:,0], points[:,1])
    #Plot centroids
    plt.scatter(kmeans.cluster_centers_[i][0], kmeans.cluster_centers_[i][1], s=100, c='red')

#Aesthetics    
ax.set_title('K-Means clustering')
ax.set_xlabel(header[0])
ax.set_ylabel(header[1])