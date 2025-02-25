
# This program demonstrates interactions with several popular vector databases.  
# Note: You'll need to install the respective database clients.  
# For example: pip install faiss-cpu annoy chumpy redis  (Redis requires additional setup for vector functionality).

# Faiss (Facebook AI Similarity Search) is a library for efficient similarity search.
import faiss
import numpy as np

# Annoy (Spotify's Approximate Nearest Neighbors Oh Yeah) is another efficient approximate nearest neighbor search library.
from annoy import AnnoyIndex

# Chumpy is a small library, offering a basic in-memory vector database.  Not as robust as Faiss or Annoy.
from chumpy import Ch

# Redis can be used as a vector database with appropriate modules/extensions.  This example is simplified and requires a Redis server running.
import redis
import pickle

# --- Faiss Example ---
def faiss_example():
    # Generate sample data (replace with your actual data)
    d = 64  # dimension
    nb = 1000  # database size
    nq = 10  # nb of queries
    np.random.seed(1234)  # make reproducible
    xb = np.random.random((nb, d)).astype('float32')
    xq = np.random.random((nq, d)).astype('float32')

    # build the index
    index = faiss.IndexFlatL2(d)  # build the index
    index.add(xb)  # add vectors to the index

    # search
    k = 4  # top k results
    D, I = index.search(xq, k)  # actual search
    print("Faiss Search Results (Distances, Indices):\n", D, I)


# --- Annoy Example ---
def annoy_example():
    d = 10  # dimensions
    t = AnnoyIndex(d, 'angular')  # Length of item vector that will be indexed
    for i in range(1000):
        v = np.random.rand(d)  # generate random vectors
        t.add_item(i, v)
    t.build(10)  # 10 trees
    t.save('test.ann')
    u = AnnoyIndex(d, 'angular')
    u.load('test.ann')
    print("Annoy Nearest Neighbor (index):", u.get_nns_by_item(0, 10)) # get 10 nearest neighbors

# --- Chumpy Example ---
def chumpy_example():
    # Chumpy is less featured, this example shows a simple addition and access
    vec1 = Ch(np.array([1, 2, 3]))
    vec2 = Ch(np.array([4, 5, 6]))
    sum_vec = vec1 + vec2
    print("Chumpy Vector Sum:", sum_vec)


# --- Redis Example (Simplified - requires a Redis server and a suitable Redis module for vectors)---
def redis_example():
    try:
        r = redis.Redis(host='localhost', port=6379, db=0) # Connect to your Redis instance

        # This part is highly dependent on the specific Redis module used for vectors
        #  Replace with the appropriate commands for your module. This is a placeholder.
        vector = np.array([1, 2, 3, 4, 5])
        r.set("myvector", pickle.dumps(vector))
        retrieved_vector = pickle.loads(r.get("myvector"))
        print("Redis Vector Retrieval:", retrieved_vector)

    except Exception as e:
        print(f"Redis Example Failed: {e}")
        print("Ensure a Redis server is running and you have a vector-compatible module installed and configured.")

# Run the examples
faiss_example()
annoy_example()
chumpy_example()
redis_example()


