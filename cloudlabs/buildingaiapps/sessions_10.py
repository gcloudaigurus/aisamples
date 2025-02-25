
# Project: Building a More Complex AI Application -  Sentiment Analysis with Topic Extraction

# This program performs sentiment analysis on text data and extracts the main topic.
# It leverages the transformers library for sentiment analysis and a simple TF-IDF approach for topic extraction.

# Install necessary libraries:  pip install transformers scikit-learn

import transformers
from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

# Function to perform sentiment analysis
def analyze_sentiment(text):
    """Performs sentiment analysis on the given text using a pre-trained model."""
    result = classifier(text)
    return result[0]['label'], result[0]['score']

# Function to extract the main topic using TF-IDF
def extract_topic(text):
    """Extracts the main topic from the text using TF-IDF."""
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text])
    feature_names = vectorizer.get_feature_names_out()
    
    # Find the word with the highest TF-IDF score
    max_index = tfidf_matrix.argmax()
    main_topic = feature_names[max_index]
    return main_topic


# Example usage
text = "This is a fantastic product! I am extremely happy with its performance and features. It's truly amazing. However, the setup process was a bit complicated."

# Perform sentiment analysis
sentiment, score = analyze_sentiment(text)
print(f"Sentiment: {sentiment}, Score: {score}")

# Extract the main topic
topic = extract_topic(text)
print(f"Main Topic: {topic}")


#Further Development:
#1.  Improve topic extraction: Explore more sophisticated topic modeling techniques like Latent Dirichlet Allocation (LDA).
#2.  Handle multiple topics: Modify the topic extraction to identify and return multiple relevant topics.
#3.  Integrate with a larger application:  Embed this functionality into a larger application, such as a customer review analyzer or social media monitoring tool.
#4.  Improve Sentiment Analysis: Fine-tune a sentiment analysis model on a specific domain for better accuracy.
#5.  Add Error Handling: Implement robust error handling to manage unexpected inputs or exceptions.
#6.  User Interface: Create a user-friendly interface (e.g., using a web framework like Flask or Streamlit) to interact with the application.



