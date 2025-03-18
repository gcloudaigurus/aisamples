# Web Crawler Q&A Agent

This project implements a Q&A agent that crawls web pages, stores their content in a vector database (ChromaDB), and uses Google's Vertex AI Gemini model to answer questions based on the stored content.

## Features

- Web crawling using requests and BeautifulSoup4
- Vector storage using ChromaDB for efficient similarity search
- Question answering using Vertex AI's Gemini-1.5-pro model
- Asynchronous API for better performance
- Comprehensive test suite

## Prerequisites

- Python 3.8 or higher
- Google Cloud Project with Vertex AI API enabled
- Google Cloud credentials configured

## Setup

1. Clone the repository and navigate to the project directory:

```bash
cd QAAgent
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Set up environment variables:

Create a `.env` file in the project root with the following:

```
GOOGLE_CLOUD_PROJECT=your-project-id
```

## Usage

1. Initialize the QA Agent:

```python
from qa_agent import QAAgent

agent = QAAgent(project_id="your-project-id")
```

2. Ingest URLs:

```python
urls = [
    "https://example.com/page1",
    "https://example.com/page2"
]
agent.ingest_urls(urls)
```

3. Ask questions:

```python
import asyncio

async def main():
    question = "What is artificial intelligence?"
    response = await agent.get_answer(question)
    print(f"Answer: {response['answer']}")
    print(f"Sources: {response['sources']}")

asyncio.run(main())
```

## Running Tests

To run the test suite:

```bash
pytest test_qa_agent.py
```

## Notes

- Make sure you have sufficient Google Cloud credits and appropriate API access
- The vector database is stored locally in the `chroma_db` directory
- For production use, consider implementing rate limiting for web crawling
- The Gemini model may have associated costs when used through Vertex AI

## License

MIT License 