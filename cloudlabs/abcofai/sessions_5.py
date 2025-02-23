#This program demonstrates sentiment analysis using the VADER (Valence Aware Dictionary and sEntiment Reasoner) lexicon.  VADER is specifically designed for social media text and is included in the `NLTK` library.


import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon if you haven't already
try:
    nltk.data.find('vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')


def analyze_sentiment(text):
    """Analyzes the sentiment of a given text using VADER."""
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    return scores


if __name__ == "__main__":
    texts = [
        "This is a great product! I love it.",
        "I hate this movie. It's terrible.",
        "The weather is okay today.  Not too bad, not too good.",
        "This is incredibly frustrating!!!",
        "This is a mixed feeling. I'm happy but also a bit sad.",
    ]

    for text in texts:
        scores = analyze_sentiment(text)
        print(f"Text: {text}")
        print(f"Sentiment Scores: {scores}")
        if scores['compound'] >= 0.05:
            print("Overall sentiment: Positive")
        elif scores['compound'] <= -0.05:
            print("Overall sentiment: Negative")
        else:
            print("Overall sentiment: Neutral")
        print("-" * 20)



#This program does the following:

#1. **Imports necessary libraries:** `nltk` for natural language processing and `SentimentIntensityAnalyzer` from the `vader` module within `nltk`.
#2. **Downloads VADER lexicon:** It checks if the VADER lexicon is already downloaded. If not, it downloads it automatically.  This only needs to be done once.
#3. **Defines `analyze_sentiment` function:** This function takes text as input, uses the `SentimentIntensityAnalyzer` to calculate sentiment scores (positive, negative, neutral, and compound), and returns the scores as a dictionary.
#4. **Tests with example texts:** The program provides a list of example texts and analyzes the sentiment of each.
#5. **Prints results:** It prints the original text, the sentiment scores, and an overall sentiment classification based on the compound score.  A compound score above 0.05 is considered positive, below -0.05 is negative, and in between is neutral.

#To run this program:

#1. **Install NLTK:**  If you don't have it, open your terminal or command prompt and run `pip install nltk`.
#2. **Save the code:** Save the code above as a Python file (e.g., `sentiment_analyzer.py`).
#3. **Run the file:** Navigate to the directory where you saved the file and run it using `python sentiment_analyzer.py`.


#This is a basic example, and NLP can encompass much more complex tasks like machine translation, text summarization, named entity recognition, and more.  This example provides a foundation for exploring these more advanced techniques.  Remember to explore the NLTK documentation for more functionalities.
