
# Project: Building a More Complex AI Application - Sentiment Analysis with Movie Review Classification

# This program demonstrates a more complex AI application by performing sentiment analysis 
# on movie reviews and classifying them as positive or negative.  It uses a simple 
# bag-of-words approach with scikit-learn for demonstration purposes.  A real-world 
# application would likely involve more sophisticated techniques like deep learning 
# (e.g., Recurrent Neural Networks or Transformers) for better accuracy.

# Import necessary libraries
import nltk
import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Download necessary NLTK data (only needs to be done once)
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)

# Sample movie review data (replace with a larger dataset for better results)
reviews = [
    ("This movie was absolutely amazing! I loved every minute of it.", "positive"),
    ("I hated this film. The acting was terrible and the plot was boring.", "negative"),
    ("A decent movie, but nothing special. It was okay.", "neutral"), #Adding a neutral example
    ("This is a masterpiece! A must-watch for all.", "positive"),
    ("I wouldn't recommend this movie to anyone. Waste of time.", "negative"),
    ("The plot was predictable, but the acting was good.", "neutral") #Adding another neutral example
]


# Preprocessing function to clean and prepare the text data
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [w for w in text.split() if w not in stop_words]
    # Join words back into a string
    return " ".join(words)


# Preprocess the reviews
processed_reviews = [(preprocess_text(review), sentiment) for review, sentiment in reviews]


# Separate features (reviews) and labels (sentiments)
reviews_processed = [review for review, sentiment in processed_reviews]
sentiments = [sentiment for review, sentiment in processed_reviews]


# Create a bag-of-words representation using CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(reviews_processed)


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, sentiments, test_size=0.2, random_state=42)


# Train a Multinomial Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train, y_train)


# Make predictions on the test set
y_pred = classifier.predict(X_test)


# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(classification_report(y_test, y_pred))

#Note:  The accuracy will be low with this small dataset. A larger dataset is needed for meaningful results.

