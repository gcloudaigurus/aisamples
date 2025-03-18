import pytest
import os
from qa_agent import QAAgent
import asyncio

# Sample test data
TEST_URLS = [
    "https://en.wikipedia.org/wiki/Artificial_intelligence",
    "https://en.wikipedia.org/wiki/Machine_learning"
]

@pytest.fixture
def qa_agent():
    # Make sure to set your Google Cloud project ID in environment variables
    project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
    if not project_id:
        pytest.skip("GOOGLE_CLOUD_PROJECT environment variable not set")
    
    agent = QAAgent(project_id=project_id)
    return agent

def test_crawl_and_ingest(qa_agent):
    """Test crawling and ingesting URLs"""
    try:
        qa_agent.ingest_urls(TEST_URLS)
    except Exception as e:
        pytest.fail(f"Failed to ingest URLs: {str(e)}")

@pytest.mark.asyncio
async def test_question_answering(qa_agent):
    """Test the question answering functionality"""
    # First ingest the test data
    qa_agent.ingest_urls(TEST_URLS)
    
    # Test questions
    test_questions = [
        "What is artificial intelligence?",
        "What is machine learning?",
    ]
    
    for question in test_questions:
        response = await qa_agent.get_answer(question)
        
        assert 'answer' in response
        assert 'sources' in response
        assert isinstance(response['answer'], str)
        assert isinstance(response['sources'], list)
        assert len(response['answer']) > 0
        assert len(response['sources']) > 0

def test_vector_store_operations(qa_agent):
    """Test vector store operations"""
    # Test clearing the vector store
    try:
        qa_agent.clear_vector_store()
    except Exception as e:
        pytest.fail(f"Failed to clear vector store: {str(e)}")
    
    # Test ingesting new documents after clearing
    try:
        qa_agent.ingest_urls(TEST_URLS[:1])  # Test with just one URL
    except Exception as e:
        pytest.fail(f"Failed to ingest URLs after clearing: {str(e)}")

if __name__ == "__main__":
    pytest.main([__file__]) 