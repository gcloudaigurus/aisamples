
# Introduction to Vector Databases: A Simple Example using FAISS

# This program demonstrates a basic use case of a vector database.  We'll use FAISS (Facebook AI Similarity Search), 
# a library optimized for efficient similarity search in high-dimensional spaces.

#  Vector databases are crucial for applications needing to find similar items based on their vector representations.
#  These vectors often represent complex data like images, text, or audio embeddings.

# Install FAISS:  pip install faiss-cpu  (or faiss-gpu if you have a compatible GPU)


import faiss
import numpy as np

# Sample data:  Imagine these are embeddings of text documents or image features.
# Each row represents a vector.
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9],
                 [10, 11, 12],
                 [1, 1, 1]], dtype='float32')

# Build an index.  We'll use the L2 distance (Euclidean distance) for similarity.  Other metrics are possible.
d = data.shape[1]  # Dimensionality of the vectors
index = faiss.IndexFlatL2(d)  # Build a flat index (suitable for smaller datasets)
index.add(data)  # Add the data to the index

# Query: Find the nearest neighbors to a new query vector.
query = np.array([[2, 3, 4]], dtype='float32')

# Search for the k nearest neighbors.
k = 2  # Number of nearest neighbors to retrieve
D, I = index.search(query, k)  # D contains distances, I contains indices of nearest neighbors

# Print results
print("Query vector:", query)
print("Distances:", D)
print("Indices of nearest neighbors:", I)

# Interpretation: The output shows the distances and indices of the two closest vectors in the database
# to the query vector.  For example, if I[0][0] is 0, it means the vector at index 0 in the 'data' array
# is the closest to the query vector.

# Note: For larger datasets, you'd want to explore more sophisticated FAISS index types (e.g., IVF, HNSW) 
# to improve search efficiency. This example is a simplified introduction to the core concepts.


#  Further exploration:
#   * Try different index types in FAISS for larger datasets.
#   * Experiment with different distance metrics.
#   * Integrate with a real-world embedding model (e.g., Sentence Transformers for text) to generate vectors from your data.
#   * Explore other vector database solutions like Milvus or Weaviate.


