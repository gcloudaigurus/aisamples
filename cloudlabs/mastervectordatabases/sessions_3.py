
import numpy as np
from scipy.spatial import distance

# Sample dataset of feature vectors (replace with your actual data)
data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [1, 1, 1]
])

# Query vector
query = np.array([2, 2, 2])


def cosine_similarity_search(data, query, top_k=1):
    """
    Performs a similarity search using cosine similarity.

    Args:
        data: A NumPy array of feature vectors.
        query: The query vector.
        top_k: The number of most similar vectors to return.

    Returns:
        A list of tuples, where each tuple contains the index of a similar vector and its cosine similarity score.  
        The list is sorted by similarity score in descending order.
    """
    similarities = []
    for i, vector in enumerate(data):
        #Cosine similarity ranges from -1 to 1.  1 indicates identical vectors, 0 means orthogonal.
        sim = 1 - distance.cosine(query, vector) #We use 1 - distance because we want higher values for greater similarity.
        similarities.append((i, sim))

    similarities.sort(key=lambda x: x[1], reverse=True)  #Sort by similarity score

    return similarities[:top_k]


def euclidean_distance_search(data, query, top_k=1):
    """
    Performs a similarity search using Euclidean distance.

    Args:
        data: A NumPy array of feature vectors.
        query: The query vector.
        top_k: The number of most similar vectors to return.

    Returns:
        A list of tuples, where each tuple contains the index of a similar vector and its Euclidean distance.
        The list is sorted by distance in ascending order (smaller distance means higher similarity).
    """
    distances = []
    for i, vector in enumerate(data):
        dist = distance.euclidean(query, vector)
        distances.append((i, dist))

    distances.sort(key=lambda x: x[1])  #Sort by Euclidean distance

    return distances[:top_k]



# Example usage: Cosine Similarity
cosine_results = cosine_similarity_search(data, query, top_k=2)
print("Cosine Similarity Search Results:", cosine_results)

# Example usage: Euclidean Distance
euclidean_results = euclidean_distance_search(data, query, top_k=2)
print("Euclidean Distance Search Results:", euclidean_results)


