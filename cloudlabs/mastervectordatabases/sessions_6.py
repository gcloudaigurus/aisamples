
# Hands-on: Setting up and Using Weaviate

# This program demonstrates basic Weaviate interaction using the Python client.
# It requires the 'weaviate-client' package.  Install it using: pip install weaviate-client

# Before running, ensure Weaviate is running.  You can download it from: https://weaviate.io/developers/weaviate/current/getting-started/installation/
#  Adjust the WEAVIATE_URL to your Weaviate instance's address.


import weaviate
from weaviate.exceptions import UnexpectedStatusCodeException

#Weaviate configuration
WEAVIATE_URL = "http://localhost:8080" #Change this to your Weaviate URL.

try:
    # Create a Weaviate client instance
    client = weaviate.Client(url=WEAVIATE_URL)

    # Define a schema for our data (e.g., for books)
    schema = {
        "classes": [
            {
                "class": "Book",
                "description": "A book with a title, author, and publication year.",
                "properties": [
                    {"name": "title", "dataType": ["string"]},
                    {"name": "author", "dataType": ["string"]},
                    {"name": "publicationYear", "dataType": ["int"]},
                ],
            }
        ]
    }

    #Check if class exists and create it if not.
    try:
        client.schema.get()
        print("Schema already exists. Skipping schema creation.")
    except UnexpectedStatusCodeException as e:
        if e.status_code == 404:
            client.schema.create(schema)
            print("Schema created successfully.")
        else:
            raise e

    # Create some data to import
    books = [
        {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "publicationYear": 1954},
        {"title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams", "publicationYear": 1979},
        {"title": "Pride and Prejudice", "author": "Jane Austen", "publicationYear": 1813},
    ]


    # Import the data into Weaviate
    for book in books:
        client.data_object.create(book, "Book")
        print(f"Book '{book['title']}' added successfully.")


    # Query Weaviate (e.g., find books by Tolkien)
    query = {
        "query": "J.R.R. Tolkien",
        "limit": 10,
    }
    
    # Perform the search
    results = client.query.get("Book", ["title", "author"], query)
    print("\nSearch Results:")
    print(results['data']['Get']['Book'])


except Exception as e:
    print(f"An error occurred: {e}")


