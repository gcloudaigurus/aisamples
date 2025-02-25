
# LLM Applications: Translation and Chatbots

# This program demonstrates a simple translation and chatbot functionality using a hypothetical LLM API.
# In a real-world scenario, you would replace these mock functions with calls to a real LLM API like OpenAI, Google Translate API etc.


# Mock LLM functions - Replace these with actual API calls in a real application

def translate_text(text, source_lang, target_lang):
    """
    Mocks a translation function.  Replace with a real translation API call.
    Args:
        text: The text to translate.
        source_lang: The source language code (e.g., "en" for English).
        target_lang: The target language code (e.g., "es" for Spanish).
    Returns:
        The translated text (or an error message).
    """
    #Simulate translation - replace this with actual API call
    translations = {
        "en": {"es": {"hello": "hola", "world": "mundo"}},
        "es": {"en": {"hola": "hello", "mundo": "world"}}
    }
    translated_words = []
    for word in text.split():
        try:
            translated_words.append(translations[source_lang][target_lang][word])
        except KeyError:
            translated_words.append(word) #Return original if not in dictionary
    return " ".join(translated_words)


def get_chatbot_response(user_input):
    """
    Mocks a chatbot response function.  Replace with a real chatbot API call.
    Args:
        user_input: The user's input.
    Returns:
        The chatbot's response.
    """
    #Simulate chatbot response - replace this with actual API call
    responses = {
        "hello": "Hi there!",
        "how are you": "I'm doing well, thank you!",
        "what's your name": "I'm a simple chatbot.",
        "default": "I didn't understand that."
    }
    for key, value in responses.items():
        if key in user_input.lower():
            return value
    return responses["default"]


# Translation example
text_to_translate = "hello world"
translated_text = translate_text(text_to_translate, "en", "es")
print(f"Original text: {text_to_translate}")
print(f"Translated text: {translated_text}")

#Chatbot example
user_input = input("Talk to the chatbot: ")
chatbot_response = get_chatbot_response(user_input)
print(f"Chatbot: {chatbot_response}")


