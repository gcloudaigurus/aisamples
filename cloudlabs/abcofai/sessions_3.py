#This program demonstrates unsupervised learning using K-Means clustering on the Iris dataset.  It's fully runnable, requiring only the `scikit-learn` library.


import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# Load the Iris dataset
iris = load_iris()
X = iris.data  # Features
y = iris.target # Labels (we won't use these directly for unsupervised learning)

# Standardize the features (important for KMeans)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determine the optimal number of clusters using the Elbow method (optional but recommended)
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


# Apply KMeans with the chosen number of clusters (e.g., 3 based on the elbow method)
kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
y_kmeans = kmeans.fit_predict(X_scaled)

# Visualize the clusters (using the first two features for simplicity)
plt.scatter(X_scaled[y_kmeans == 0, 0], X_scaled[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
plt.scatter(X_scaled[y_kmeans == 1, 0], X_scaled[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
plt.scatter(X_scaled[y_kmeans == 2, 0], X_scaled[y_kmeans == 2, 1], s=100, c='green', label='Cluster 3')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids')
plt.title('Clusters of Iris Dataset')
plt.xlabel('Sepal Length') # Assuming first feature is Sepal Length
plt.ylabel('Sepal Width') # Assuming second feature is Sepal Width
plt.legend()
plt.show()

print("Cluster labels:", y_kmeans)



#Before running:

#1. **Install scikit-learn:**  If you don't have it, open your terminal or command prompt and run `pip install scikit-learn` or `conda install scikit-learn` (if using Anaconda).
#2. **Run the script:** Save the code as a `.py` file (e.g., `kmeans_iris.py`) and run it from your terminal using `python kmeans_iris.py`.


#The program will:

#1. Load the Iris dataset.
#2. Standardize the features (important for KMeans to prevent features with larger values from dominating).
#3. Use the Elbow method to help determine a good number of clusters (visually inspect the plot).
#4. Apply KMeans clustering with the chosen number of clusters.
#5. Visualize the resulting clusters using a scatter plot.
#6. Print the cluster labels assigned to each data point.


#Remember that the choice of the number of clusters (in this case, influenced by the Elbow method) is crucial and can impact the results.  Experiment with different numbers of clusters to see how the results change.  Other unsupervised learning algorithms (like DBSCAN or hierarchical clustering) could also be used with this dataset.
