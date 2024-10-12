from sklearn.cluster import KMeans
import numpy as np

# Generate some sample data
X = np.random.rand(100, 5)

# Create a KMeans instance
kmeans = KMeans(n_clusters=3)

# Fit the model to the data
kmeans.fit(X)

# Get cluster centroids
centroids = kmeans.cluster_centers_
print(f"centroids.shape is {centroids.shape}")
# Get cluster labels for each data point
labels = kmeans.labels_

print(f"labels.shape is {labels.shape}")