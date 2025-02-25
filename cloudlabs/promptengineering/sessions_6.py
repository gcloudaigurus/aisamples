
# Prompt Engineering for Specific Tasks:  Sentiment Analysis

# This program demonstrates prompt engineering for sentiment analysis.  We'll use a simple example 
# without a large language model (LLM) for simplicity.  In a real-world scenario, you'd use an LLM 
# like GPT-3, etc. and a suitable library to interact with it.

# The core idea is crafting effective prompts to guide the LLM toward the desired output.


def analyze_sentiment(text, prompt_type="simple"):
    """
    Analyzes the sentiment of a given text using different prompt engineering techniques.

    Args:
        text: The input text to analyze.
        prompt_type: The type of prompt to use ("simple", "detailed", or "comparative"). Defaults to "simple".

    Returns:
        A dictionary containing the sentiment analysis result.  For this example, only positive/negative.  LLMs can do much more nuanced results
    """

    # Simple Prompt:  Directly asks for sentiment
    if prompt_type == "simple":
        if "happy" in text.lower() or "good" in text.lower() or "love" in text.lower():
            return {"sentiment": "positive"}
        elif "sad" in text.lower() or "bad" in text.lower() or "hate" in text.lower():
            return {"sentiment": "negative"}
        else:
            return {"sentiment": "neutral"}

    # Detailed Prompt:  Asks for a justification for the sentiment
    elif prompt_type == "detailed":  #This would require LLM
        #In a real LLM application, you would send a detailed prompt like:
        #"Analyze the sentiment of the following text and provide a justification: [text]"
        return {"sentiment": "Not implemented for this simple example. Requires LLM"}

    # Comparative Prompt:  Compares sentiment across multiple texts  (This too would require an LLM)
    elif prompt_type == "comparative": #This would require LLM
       #In a real LLM application,  you might ask:
       #"Compare the sentiment of these two texts and explain the differences: Text 1: [text1], Text 2: [text2]"
       return {"sentiment": "Not implemented for this simple example. Requires LLM"}


    else:
        return {"error": "Invalid prompt type"}



# Example Usage
text1 = "I am feeling happy today!"
text2 = "This is a terrible day."
text3 = "The weather is okay."


print(f"Simple Prompt - Text 1: {analyze_sentiment(text1, 'simple')}") #Simple prompt
print(f"Simple Prompt - Text 2: {analyze_sentiment(text2, 'simple')}") #Simple prompt
print(f"Simple Prompt - Text 3: {analyze_sentiment(text3, 'simple')}") #Simple prompt


print(f"Detailed Prompt - Text 1: {analyze_sentiment(text1, 'detailed')}") #Detailed prompt (Not implemented here)
print(f"Comparative Prompt - Text 1 & 2: {analyze_sentiment(text1, 'comparative')}") #Comparative prompt (Not implemented here)


