from typing import List, Dict, Optional
import os
from google.cloud import aiplatform
from vertexai.preview.generative_models import GenerativeModel
import vertexai
from web_crawler import WebCrawler
from vector_store import VectorStore
import logging
from dotenv import load_dotenv

class QAAgent:
    def __init__(self, project_id: str, location: str = "us-central1"):
        """
        Initialize the QA Agent.
        
        Args:
            project_id (str): Google Cloud project ID
            location (str): Google Cloud location
        """
        load_dotenv()
        
        # Initialize Vertex AI
        vertexai.init(project=project_id, location=location)
        
        self.crawler = WebCrawler()
        self.vector_store = VectorStore()
        self.model = GenerativeModel("gemini-1.5-pro")
        
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def ingest_urls(self, urls: List[str]) -> None:
        """
        Crawl URLs and store their content in the vector store.
        
        Args:
            urls (List[str]): List of URLs to process
        """
        # Crawl the webpages
        documents = self.crawler.crawl_multiple_pages(urls)
        
        # Store in vector database
        self.vector_store.add_documents(documents)

    async def get_answer(self, question: str) -> Dict[str, str]:
        """
        Get an answer for a question using the vector store and Vertex AI.
        
        Args:
            question (str): The question to answer
            
        Returns:
            Dict[str, str]: Dictionary containing the answer and sources
        """
        try:
            # Get relevant documents from vector store
            relevant_docs = self.vector_store.search(question)
            
            if not relevant_docs:
                return {
                    'answer': 'I could not find any relevant information to answer your question.',
                    'sources': []
                }
            
            # Prepare context for the model
            context = "Based on the following information:\n\n"
            sources = []
            
            for doc in relevant_docs:
                context += f"From {doc['metadata']['url']}:\n{doc['content']}\n\n"
                sources.append(doc['metadata']['url'])
            
            # Prepare the prompt
            prompt = f"""{context}
            
            Please answer this question: {question}
            
            Provide a clear and concise answer based only on the information provided above."""
            
            # Get response from Vertex AI
            response = await self.model.generate_content_async(prompt)
            
            return {
                'answer': response.text,
                'sources': sources
            }
            
        except Exception as e:
            self.logger.error(f"Error getting answer: {str(e)}")
            return {
                'answer': f'An error occurred while processing your question: {str(e)}',
                'sources': []
            }

    def clear_vector_store(self) -> None:
        """
        Clear all documents from the vector store.
        """
        try:
            self.vector_store.collection.delete()
            self.vector_store = VectorStore()  # Reinitialize the collection
            self.logger.info("Vector store cleared successfully")
        except Exception as e:
            self.logger.error(f"Error clearing vector store: {str(e)}")
            raise 