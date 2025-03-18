import chromadb
from chromadb.utils import embedding_functions
from typing import Dict, List, Optional
import logging

class VectorStore:
    def __init__(self, persist_directory: str = "chroma_db"):
        """
        Initialize the vector store with ChromaDB.
        
        Args:
            persist_directory (str): Directory to persist the database
        """
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection(
            name="webpage_content",
            embedding_function=embedding_functions.DefaultEmbeddingFunction()
        )
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def add_documents(self, documents: List[Dict[str, str]]) -> None:
        """
        Add documents to the vector store.
        
        Args:
            documents (List[Dict[str, str]]): List of documents with url, title, and content
        """
        try:
            documents_to_add = []
            metadatas = []
            ids = []
            
            for i, doc in enumerate(documents):
                documents_to_add.append(doc['content'])
                metadatas.append({
                    'url': doc['url'],
                    'title': doc['title']
                })
                ids.append(f"doc_{i}")
            
            self.collection.add(
                documents=documents_to_add,
                metadatas=metadatas,
                ids=ids
            )
            self.logger.info(f"Successfully added {len(documents)} documents to vector store")
            
        except Exception as e:
            self.logger.error(f"Error adding documents to vector store: {str(e)}")
            raise

    def search(self, query: str, n_results: int = 3) -> List[Dict]:
        """
        Search for relevant documents based on a query.
        
        Args:
            query (str): The search query
            n_results (int): Number of results to return
            
        Returns:
            List[Dict]: List of relevant documents with their metadata
        """
        try:
            results = self.collection.query(
                query_texts=[query],
                n_results=n_results
            )
            
            documents = []
            for i in range(len(results['documents'][0])):
                documents.append({
                    'content': results['documents'][0][i],
                    'metadata': results['metadatas'][0][i]
                })
            
            return documents
            
        except Exception as e:
            self.logger.error(f"Error searching vector store: {str(e)}")
            return [] 