import asyncio
import os
from qa_agent import QAAgent
from typing import List
import logging
from dotenv import load_dotenv

class QAInterface:
    def __init__(self):
        load_dotenv()
        self.project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
        if not self.project_id:
            raise EnvironmentError("GOOGLE_CLOUD_PROJECT environment variable not set")
        
        self.agent = QAAgent(project_id=self.project_id)
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def get_urls_from_user(self) -> List[str]:
        """Get URLs from user input."""
        print("\nEnter URLs to crawl (one per line). Press Enter twice to finish:")
        urls = []
        while True:
            url = input().strip()
            if not url:
                break
            if url.startswith(('http://', 'https://')):
                urls.append(url)
            else:
                print("Invalid URL. Please include http:// or https://")
        return urls

    async def ask_questions(self):
        """Interactive question-asking loop."""
        print("\nYou can now ask questions (type 'exit' to quit):")
        while True:
            question = input("\nEnter your question: ").strip()
            if question.lower() == 'exit':
                break
            
            if not question:
                continue
                
            try:
                response = await self.agent.get_answer(question)
                print("\nAnswer:", response['answer'])
                if response['sources']:
                    print("\nSources:")
                    for source in response['sources']:
                        print(f"- {source}")
            except Exception as e:
                self.logger.error(f"Error getting answer: {str(e)}")
                print(f"\nError: {str(e)}")

    def display_menu(self):
        """Display the main menu."""
        print("\n=== QA Agent Menu ===")
        print("1. Crawl new web pages")
        print("2. Ask questions")
        print("3. Clear database")
        print("4. Exit")
        return input("Select an option (1-4): ").strip()

    async def run(self):
        """Main run loop."""
        print("Welcome to the QA Agent Interface!")
        
        while True:
            choice = self.display_menu()
            
            if choice == '1':
                urls = self.get_urls_from_user()
                if urls:
                    print(f"\nCrawling {len(urls)} URLs...")
                    try:
                        self.agent.ingest_urls(urls)
                        print("Successfully crawled and stored web pages!")
                    except Exception as e:
                        self.logger.error(f"Error crawling URLs: {str(e)}")
                        print(f"Error: {str(e)}")
                else:
                    print("No valid URLs provided.")
                    
            elif choice == '2':
                await self.ask_questions()
                
            elif choice == '3':
                try:
                    self.agent.clear_vector_store()
                    print("\nDatabase cleared successfully!")
                except Exception as e:
                    self.logger.error(f"Error clearing database: {str(e)}")
                    print(f"Error: {str(e)}")
                    
            elif choice == '4':
                print("\nThank you for using QA Agent. Goodbye!")
                break
                
            else:
                print("\nInvalid option. Please try again.")

def main():
    try:
        interface = QAInterface()
        asyncio.run(interface.run())
    except Exception as e:
        print(f"Error initializing QA Agent: {str(e)}")
        print("Please make sure you have set up your Google Cloud credentials and environment variables correctly.")

if __name__ == "__main__":
    main() 