
import numpy as np

# Vector embeddings represent words or other semantic units as dense vectors of real numbers.
# These vectors capture semantic meaning, allowing for relationships between words to be represented mathematically.

# Example:  We'll create a simple example with three words: "king", "queen", "man".
# We'll use a simplified embedding approach (not a sophisticated pre-trained model).

# Define word embeddings as NumPy arrays.  In reality, these would be learned from large datasets.
king_embedding = np.array([0.8, 0.7, 0.9, 0.6, 0.5])  #Example embedding for "king"
queen_embedding = np.array([0.7, 0.8, 0.8, 0.7, 0.6]) #Example embedding for "queen"
man_embedding = np.array([0.6, 0.5, 0.7, 0.4, 0.3])   #Example embedding for "man"


# Function to calculate cosine similarity - a common way to measure semantic similarity between vectors.
def cosine_similarity(a, b):
    """Computes the cosine similarity between two vectors."""
    dot_product = np.dot(a, b)
    magnitude_a = np.linalg.norm(a)
    magnitude_b = np.linalg.norm(b)
    if magnitude_a == 0 or magnitude_b == 0:
        return 0  # Handle cases where a vector has zero magnitude.
    return dot_product / (magnitude_a * magnitude_b)


# Calculate and print the cosine similarity between "king" and "queen".
similarity_kq = cosine_similarity(king_embedding, queen_embedding)
print(f"Cosine similarity between 'king' and 'queen': {similarity_kq}")


# Calculate and print the cosine similarity between "king" and "man".
similarity_km = cosine_similarity(king_embedding, man_embedding)
print(f"Cosine similarity between 'king' and 'man': {similarity_km}")


# The higher the cosine similarity, the more semantically similar the words are considered to be.

# Note: This is a highly simplified illustration. Real-world vector embeddings are typically much higher-dimensional (e.g., 300, 768 dimensions)
# and are learned using complex neural network models trained on massive text corpora (like Word2Vec, GloVe, FastText, BERT etc.).

