
import numpy as np
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# Generate sample data (replace with your own data)
np.random.seed(0)
X = np.random.rand(100, 50)  # 100 samples, 50 features

#-----------------------------------------------------------------------------
# Principal Component Analysis (PCA)
# PCA is a linear dimensionality reduction technique that aims to find the 
# principal components, which are orthogonal directions of maximum variance 
# in the data.  It reduces dimensionality by projecting the data onto a 
# lower-dimensional subspace spanned by the principal components.
#-----------------------------------------------------------------------------
pca = PCA(n_components=2) # Reduce to 2 dimensions
X_pca = pca.fit_transform(X)

#-----------------------------------------------------------------------------
# Truncated Singular Value Decomposition (SVD)
# SVD is another linear dimensionality reduction technique, closely related to 
# PCA. It's particularly useful for dealing with high-dimensional sparse data.
#-----------------------------------------------------------------------------
svd = TruncatedSVD(n_components=2) #Reduce to 2 dimensions
X_svd = svd.fit_transform(X)

#-----------------------------------------------------------------------------
# t-distributed Stochastic Neighbor Embedding (t-SNE)
# t-SNE is a non-linear dimensionality reduction technique that is particularly 
# good at visualizing high-dimensional data in a low-dimensional space. It 
# focuses on preserving local neighborhood structures in the data.  It can be 
# computationally expensive for large datasets.
#-----------------------------------------------------------------------------
tsne = TSNE(n_components=2, perplexity=30, n_iter=300) # perplexity and n_iter are hyperparameters to tune.
X_tsne = tsne.fit_transform(X)


# Plot the results
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.scatter(X_pca[:, 0], X_pca[:, 1])
plt.title('PCA')

plt.subplot(1, 3, 2)
plt.scatter(X_svd[:, 0], X_svd[:, 1])
plt.title('SVD')

plt.subplot(1, 3, 3)
plt.scatter(X_tsne[:, 0], X_tsne[:, 1])
plt.title('t-SNE')

plt.show()


