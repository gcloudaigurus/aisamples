
# Real-world Application: Sentiment Analysis of Movie Reviews

# Case Study: Analyzing movie review text to determine if the sentiment is positive, negative, or neutral.

# We'll use the VADER (Valence Aware Dictionary and sEntiment Reasoner) lexicon, 
# which is specifically designed for sentiment analysis of social media text (including movie reviews).

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Sample movie review data (replace with your own dataset for a real-world application)
reviews = [
    "This movie was absolutely amazing! I loved every minute of it.",  #Positive
    "I found the plot to be confusing and the acting subpar.  A major disappointment.", #Negative
    "It was an okay movie.  Nothing special, but not terrible either.", #Neutral
    "A masterpiece of cinematic storytelling!  A must-see!", #Positive
    "Completely wasted my time and money.  Avoid at all costs!", #Negative
]

analyzer = SentimentIntensityAnalyzer() #Initialize VADER sentiment analyzer

# Function to analyze sentiment and classify it
def analyze_sentiment(text):
    scores = analyzer.polarity_scores(text)
    compound_score = scores['compound']

    if compound_score >= 0.05:
        return "Positive"
    elif compound_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Analyze each review and print the results
for review in reviews:
    sentiment = analyze_sentiment(review)
    print(f"Review: {review}\nSentiment: {sentiment}\n")


#Further Development:

# 1.  Larger Dataset:  Use a much larger dataset of movie reviews (e.g., from IMDB).
# 2.  Data Cleaning: Implement techniques to clean the text data (remove punctuation, handle slang, etc.) before analysis.
# 3.  Machine Learning Models: Explore more advanced sentiment analysis techniques using machine learning models (e.g., Naive Bayes, SVM, Recurrent Neural Networks) for improved accuracy.
# 4.  Aspect-Based Sentiment Analysis: Analyze sentiment towards specific aspects of the movie (e.g., plot, acting, direction).
# 5.  Visualization: Create visualizations (e.g., bar charts, word clouds) to represent the sentiment analysis results.


#To run this code, you'll need to install the vaderSentiment library:
#pip install vaderSentiment

