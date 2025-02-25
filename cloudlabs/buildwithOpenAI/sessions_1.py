
# Introduction to AI and OpenAI's Ecosystem - Sample Program

# This program demonstrates a basic interaction with OpenAI's API using the `openai` library.
# It requires an OpenAI API key.  You should obtain one from your OpenAI account and set it as an environment variable named OPENAI_API_KEY.

# Install the necessary library: pip install openai

import openai
import os

# Set your OpenAI API key.  The following line is crucial for the program to function.
# Ensure your API key is securely stored as an environment variable and not hardcoded in your scripts.
openai.api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is set.  Handle the case where the key is missing.
if not openai.api_key:
    print("Error: OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
    exit(1)


# Example 1: Generating text using the GPT-3 model.
def generate_text(prompt):
    """Generates text using OpenAI's API."""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003", # Specify the model to use.  Other models are available.
            prompt=prompt,
            max_tokens=150, # Limit the length of the generated text.
            n=1, # Number of completions to generate.
            stop=None, # A token to stop generation (optional).
            temperature=0.7, # Controls randomness. Higher values produce more creative text.
        )
        return response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        print(f"OpenAI API error: {e}")
        return None


# Example usage:  Let's ask GPT-3 a question.
user_prompt = "What is artificial intelligence?"
generated_text = generate_text(user_prompt)

if generated_text:
    print(f"User prompt: {user_prompt}\n")
    print(f"Generated text:\n{generated_text}\n")


# Example 2:  Illustrating potential for different tasks (this is just a placeholder)
# OpenAI's ecosystem supports various tasks beyond text generation. This is a simplified example.

# This section would typically involve more complex interactions with the API,  such as using embeddings for semantic search or fine-tuning models.

# For example, you could use embeddings to find similar documents or use a different model for translation.
#  Refer to OpenAI's API documentation for more advanced functionalities.

print("This is a basic introduction. Explore OpenAI's API documentation for more capabilities.")



