
# This program demonstrates interacting with an LLM API (using OpenAI's API as an example).  
# It requires the 'openai' library. Install it using: pip install openai

# Remember to set your OpenAI API key as an environment variable named "OPENAI_API_KEY".
# You can obtain an API key from the OpenAI website.

import openai
import os

# Set your OpenAI API key.  This is crucial for authentication.
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_completion_from_openai(prompt):
    """
    This function sends a prompt to the OpenAI API and returns the model's response.
    It handles potential errors during API interaction.
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Specify the desired OpenAI model.  Other models may be available.
            prompt=prompt,
            max_tokens=150, # Limit the response length. Adjust as needed.
            n=1,  # Number of completions to generate.
            stop=None, #  Optional: Specify a stop sequence to halt generation.
            temperature=0.7, # Controls randomness. 0.0 is deterministic, higher values are more creative.
        )
        return response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        print(f"OpenAI API Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None



if __name__ == "__main__":
    # Example usage:  Get a response to a user prompt.
    user_prompt = "Write a short poem about a cat."
    response = get_completion_from_openai(user_prompt)

    if response:
        print(f"AI Response:\n{response}")
    else:
        print("Failed to get a response from the OpenAI API.")


#Further Development:
#1. Error handling could be improved, e.g., retry mechanisms for transient API errors.
#2.  Integration with other cloud services (e.g., cloud storage for storing prompts and responses) could be added.
#3. The program could be extended to handle user input more robustly (e.g., using a command-line interface or a web framework).
#4.  Explore other LLM providers' APIs (e.g., Cohere, AI21 Labs) and integrate them into the code for comparison.
#5. Implement more sophisticated prompt engineering techniques to control the output quality.


