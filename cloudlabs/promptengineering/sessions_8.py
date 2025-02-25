
# This program demonstrates evaluating and improving prompts for a sentiment analysis task.

# We'll use a simplified example with pre-defined sentiment labels.  In a real-world scenario,
# you'd use a pre-trained model or build one to analyze sentiment.

# Initial prompt:  Simple and potentially ambiguous.
initial_prompt = "Analyze the sentiment of this text:  The movie was okay."


def analyze_sentiment(text, prompt):
    """
    This function simulates sentiment analysis.  Replace this with a real sentiment analysis model 
    for more accurate results.
    """
    #  A very basic example - replace with a proper sentiment analysis model.
    if "good" in text.lower() or "great" in text.lower() or "amazing" in text.lower():
      return "positive"
    elif "bad" in text.lower() or "terrible" in text.lower() or "awful" in text.lower():
      return "negative"
    else:
      return "neutral"

# Evaluate the initial prompt.
text = "The movie was okay."
initial_sentiment = analyze_sentiment(text, initial_prompt)
print(f"Initial Prompt: {initial_prompt}")
print(f"Sentiment of '{text}' using initial prompt: {initial_sentiment}") # Likely neutral, which might not capture the nuance


# Improved prompt: More specific instructions.
improved_prompt = "Analyze the sentiment of this text.  Provide a label of 'positive', 'negative', or 'neutral'.  Consider the overall tone and emotional expression."

improved_sentiment = analyze_sentiment(text, improved_prompt)  #The analysis itself doesn't change based on the prompt in this simplified example
print(f"\nImproved Prompt: {improved_prompt}")
print(f"Sentiment of '{text}' using improved prompt: {improved_sentiment}") # Still neutral, but the prompt is better structured



#Further improvement: providing context or examples

contextual_prompt = "Analyze the sentiment of the following movie review:  'The movie was okay.'   Consider that 'okay' can sometimes indicate mild disappointment or just a lack of strong feelings, rather than strong positivity.  Examples:  'Okay' in 'The movie was okay, but nothing special' is likely neutral to slightly negative. 'The movie was okay considering the low budget' indicates a positive sentiment relative to expectations. Provide a label: 'positive', 'negative', or 'neutral'."

contextual_sentiment = analyze_sentiment(text, contextual_prompt) # still neutral in this simplified example.
print(f"\nContextual Prompt: {contextual_prompt}")
print(f"Sentiment of '{text}' using contextual prompt: {contextual_sentiment}")


# Note: The sentiment analysis here is very basic.  Real-world applications would involve sophisticated 
# models (like those from transformers libraries) and techniques for evaluating prompt effectiveness 
# (like human evaluation or comparing results across multiple models).  This example focuses on the 
# iterative prompt improvement process itself.

#To make this fully functional, replace the `analyze_sentiment` function with a proper sentiment analysis model.  For instance, you could use the `transformers` library.

