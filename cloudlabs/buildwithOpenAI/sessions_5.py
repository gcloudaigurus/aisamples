
# Import necessary libraries
import sentence_transformers
from sklearn.metrics.pairwise import cosine_similarity

# Sample sentences for our search index
sentences = [
    "This is an example sentence.",
    "Each sentence is converted into an embedding.",
    "Semantic search allows us to find similar sentences.",
    "This is another example sentence, but slightly different.",
    "Embeddings are vector representations of text."
]

# Load a pre-trained Sentence Transformer model.  There are many available; 
# this one is a good all-purpose choice, but you might find others better suited 
# to your specific application.
model = sentence_transformers.SentenceTransformer('all-mpnet-base-v2')


# Generate embeddings for each sentence
embeddings = model.encode(sentences)

# Function to perform semantic search
def semantic_search(query, embeddings, sentences, top_k=3):  #top_k defines how many results we want
    """
    Performs a semantic search given a query sentence.

    Args:
        query: The search query sentence.
        embeddings: A NumPy array of sentence embeddings.
        sentences: A list of sentences corresponding to the embeddings.
        top_k: The number of top results to return.

    Returns:
        A list of tuples, where each tuple contains a sentence and its cosine similarity score.
    """
    query_embedding = model.encode(query)  # Generate embedding for the query sentence

    # Calculate cosine similarity between the query embedding and all sentence embeddings.
    similarities = cosine_similarity([query_embedding], embeddings)[0]

    # Get the indices of the top k most similar sentences
    top_k_indices = similarities.argsort()[-top_k:][::-1] #argsort returns indices that would sort the array. We reverse it to get top k

    # Return the top k sentences and their similarity scores
    results = [(sentences[i], similarities[i]) for i in top_k_indices]
    return results


# Example usage:
query = "Find sentences about sentence embeddings"
results = semantic_search(query, embeddings, sentences)

# Print the search results
print(f"Search query: {query}")
for sentence, score in results:
    print(f"Sentence: {sentence}, Similarity Score: {score:.4f}")



#Further improvements could include:
# - Using a larger dataset of sentences for a more comprehensive search index.
# - Implementing techniques to handle different sentence lengths and improve efficiency for large datasets.
# - Exploring different Sentence Transformer models to optimize for specific tasks or domains.
# - Adding a mechanism to persist the embeddings to avoid recalculating them each time.


