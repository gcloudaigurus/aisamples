
# Import the necessary libraries.  You'll need to install the OpenAI library: pip install openai
import openai

# Set your OpenAI API key.  **REPLACE THIS WITH YOUR ACTUAL API KEY**
openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_text(prompt, model="text-davinci-003", max_tokens=150, temperature=0.7):
    """
    Generates text using the OpenAI API.

    Args:
        prompt: The text prompt to use for generation.
        model: The OpenAI model to use (default: text-davinci-003).  Other models may be available, check OpenAI's documentation.
        max_tokens: The maximum number of tokens to generate (default: 150).  Tokens are essentially units of text.
        temperature: Controls the randomness of the generated text (default: 0.7). Higher values = more random.

    Returns:
        The generated text, or an error message if something goes wrong.
    """
    try:
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=max_tokens,
            n=1, # Number of completions to generate.  We only want one here.
            stop=None, #  Optional: Specify a stop sequence to halt generation.  e.g., ["."]
            temperature=temperature,
        )
        generated_text = response.choices[0].text.strip()
        return generated_text
    except openai.error.OpenAIError as e:
        return f"An error occurred: {e}"


# Example usage:
prompt = "Write a short story about a robot who learns to love."
generated_story = generate_text(prompt)
print(generated_story)


prompt = "Give me a list of 5 things to do in Paris"
generated_list = generate_text(prompt, max_tokens=50, temperature=0.5) # Lower temperature for a more focused list
print(generated_list)


#Experiment with different prompts, models (if you have access), max_tokens, and temperature to see how it affects the output.  
#Remember to check OpenAI's API documentation for the latest models and parameters.

#Note: Using a higher temperature will result in more creative but potentially less coherent text.
#A lower temperature will produce more focused and predictable text.

#Rate limits apply to the OpenAI API, so be mindful of how many requests you make.

