
# Import the OpenAI library
import openai

# Set your OpenAI API key.  **REPLACE THIS WITH YOUR ACTUAL API KEY**
openai.api_key = "YOUR_OPENAI_API_KEY"

# Define a function to interact with the OpenAI API's Completion endpoint
def get_completion(prompt, model="text-davinci-003", max_tokens=150, n=1, stop=None, temperature=0.7):
    """
    This function sends a prompt to the OpenAI API and returns the generated text.

    Args:
        prompt (str): The prompt to send to the API.
        model (str, optional): The model to use. Defaults to "text-davinci-003".
        max_tokens (int, optional): The maximum number of tokens to generate. Defaults to 150.
        n (int, optional): The number of completions to generate. Defaults to 1.
        stop (str or list, optional): A sequence of strings that will stop generation. Defaults to None.
        temperature (float, optional): Controls the randomness of the generated text. Defaults to 0.7.

    Returns:
        str: The generated text.  Returns an error message if there's an API issue.
    """
    try:
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=max_tokens,
            n=n,
            stop=stop,
            temperature=temperature,
        )
        # Accessing the generated text from the API response
        generated_text = response.choices[0].text.strip()
        return generated_text
    except openai.error.OpenAIError as e:
        return f"An error occurred: {e}"


# Example usage:  A simple prompt
prompt = "Write a short poem about a cat."
completion = get_completion(prompt)
print(f"Prompt: {prompt}\nCompletion:\n{completion}")


# Example usage:  A more complex prompt with multiple parameters
prompt2 = "Translate the following English text to French:  'Hello, how are you?'"
completion2 = get_completion(prompt2, max_tokens=30, temperature=0.5) # Lower temperature for more deterministic translation
print(f"\nPrompt: {prompt2}\nCompletion:\n{completion2}")


# Example demonstrating error handling (intentionally using an invalid API key - comment out if you have a valid one)

#openai.api_key = "invalid-api-key"  
#invalid_completion = get_completion("This should fail.")
#print(f"\nAttempt with invalid key:\n{invalid_completion}")


