
# Install the Pinecone client library
# pip install pinecone-client

# Import the Pinecone library
import pinecone

# Set your API key and environment
# Replace with your actual API key and environment
API_KEY = "YOUR_PINECONE_API_KEY"  
ENVIRONMENT = "YOUR_PINECONE_ENVIRONMENT" # e.g., "gcp-starter"

# Initialize the Pinecone connection
try:
    pinecone.init(api_key=API_KEY, environment=ENVIRONMENT)
except Exception as e:
    print(f"Error initializing Pinecone: {e}")
    exit(1)


# Check connection
try:
    print(f"Pinecone version: {pinecone.__version__}")
    print("Successfully connected to Pinecone!")

except Exception as e:
    print(f"Error connecting to Pinecone: {e}")
    exit(1)



# Create a Pinecone index (if it doesn't exist)
index_name = "my-first-index" #Choose a name for your index

try:
    index = pinecone.Index(index_name)
    print(f"Index '{index_name}' already exists.")

except Exception as e:
    if "Index does not exist" in str(e):
      # Create the index.  Adjust the metric and dimension as needed for your data.
      pinecone.create_index(index_name, dimension=10, metric="cosine") #dimension is the vector length, metric is the distance function used
      index = pinecone.Index(index_name)
      print(f"Index '{index_name}' created successfully.")
    else:
      print(f"An unexpected error occurred: {e}")
      exit(1)


# Upsert vectors (add or update vectors in the index)
vectors = [
    ("vec1", [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]),
    ("vec2", [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0]),
]


try:
    index.upsert(vectors=vectors)  # upsert adds if vector doesn't exist or updates if it does
    print("Vectors upserted successfully.")
except Exception as e:
    print(f"Error upserting vectors: {e}")
    exit(1)


# Query the index
query_vector = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1]
try:
    results = index.query(vector=query_vector, top_k=1)
    print("Query results:")
    print(results)
except Exception as e:
    print(f"Error querying the index: {e}")
    exit(1)


# Delete the index (optional - comment out if you want to keep the index for later use)
# index.delete(deleteAll=True) #Use with caution!  This will delete all your data!
# print("Index deleted successfully.")

