import numpy as np
import matplotlib.pyplot as plt
class Kmeans:
    def __init__(self, num_cluster, max_iter=10):
        self.num_cluster = num_cluster
        self.max_iter = max_iter
    
    def fit(self, X):
        '''
        X.shape = [num_sample, num_feature]
        '''
        centroids = np.array(X[np.random.choice(X.shape[0], self.num_cluster, replace=False)])
        
        self.centroids =  centroids.T #dim(num_feature, num_centroids)
        print(self.centroids[None, :, :].shape)
        
        for iter in range(self.max_iter):
            print(iter)
            dist = np.linalg.norm(X[:, :, None] - self.centroids[None, :, :], axis = 1) #dim(num_sample, num_centroid)
            new_id = np.argmin(dist, axis = 1) #dim(num_sample)
            
            new_centroids = np.array([X[new_id == label].mean(axis = 0) for label in range(self.num_cluster)])
            
            self.centroids = new_centroids.T

X = np.random.rand(20,2)
            
kmeans = Kmeans(num_cluster=4)
kmeans.fit(X)
print(kmeans.centroids)

plt.figure()
plt.scatter(X[:,0], X[:,1])
plt.scatter(kmeans.centroids[0,:], kmeans.centroids[1,:], c = 'r')
plt.savefig('k_means.png')


                