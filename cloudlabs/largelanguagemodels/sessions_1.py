
# Introduction to Large Language Models (LLMs) - Sample Python Program

# This program demonstrates a basic interaction with an LLM using the OpenAI API.
# It requires the 'openai' library.  Install it using: pip install openai

# Remember to set your OpenAI API key as an environment variable named "OPENAI_API_KEY"
# You can get an API key from https://platform.openai.com/account/api-keys

import openai
import os

# Set your OpenAI API key (ensure OPENAI_API_KEY is set in your environment)
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_llm_response(prompt):
    """
    This function sends a prompt to the OpenAI API and returns the model's response.

    Args:
        prompt: The text prompt to send to the LLM.

    Returns:
        The LLM's response as a string.  Returns an error message if there's an issue.
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Specify the LLM model (choose an available model)
            prompt=prompt,
            max_tokens=150,  # Limit the response length
            n=1,  # Number of responses to generate
            stop=None,  # Optional: specify a stop sequence
            temperature=0.7, # Controls the randomness of the response (0.0 - deterministic, 1.0 - highly random)
        )
        return response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        return f"An error occurred: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


if __name__ == "__main__":
    # Example usage:
    user_prompt = "Write a short poem about a cat sitting in a sunbeam."
    llm_output = get_llm_response(user_prompt)
    print(f"User Prompt: {user_prompt}\n")
    print(f"LLM Response:\n{llm_output}")


    #Another example
    user_prompt = "Translate 'Hello, how are you?' into Spanish"
    llm_output = get_llm_response(user_prompt)
    print(f"\nUser Prompt: {user_prompt}\n")
    print(f"LLM Response:\n{llm_output}")


    #Example demonstrating error handling.  Uncomment to test.  Note that this is not a valid model.
    #user_prompt = "This is a test"
    #llm_output = get_llm_response(user_prompt, model="invalid-model-name")
    #print(f"\nUser Prompt: {user_prompt}\n")
    #print(f"LLM Response:\n{llm_output}")


