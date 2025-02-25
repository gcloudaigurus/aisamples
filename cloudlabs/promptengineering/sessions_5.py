
# Handling Ambiguity and Bias in Prompts: A Sample Python Program

# This program demonstrates how to mitigate ambiguity and bias in prompts 
# by providing clear instructions, diverse examples, and considering potential biases.

# Ambiguity Example:  The prompt "Write about dogs" is ambiguous.  
# What kind of dogs? What aspects should be discussed?

# Bias Example: A prompt like "Describe a typical doctor" might implicitly 
# bias the response towards a specific gender or race, reflecting societal stereotypes.


def generate_text(prompt, examples=None, constraints=None):
    """
    Generates text based on a prompt, mitigating ambiguity and bias.

    Args:
        prompt: The main prompt (string).
        examples: A list of example text completions (list of strings), to reduce ambiguity and guide style.
        constraints: A dictionary of constraints to reduce bias (e.g., {"gender": ["male", "female"], "race": ["white", "black", "asian"]}).  This feature is rudimentary and needs more sophisticated handling in real-world scenarios.


    Returns:
        A string containing the generated text.  (In a real application, this would likely use a language model)
    """

    #In a real-world scenario, this would call a language model API or use a large language model.
    #For this example, we'll simulate a simple response based on the prompt and examples.

    output = ""
    if examples:
        output += "Examples provided:\n"
        for example in examples:
            output += example + "\n"
    
    if constraints:
        #Rudimentary constraint checking –  this needs substantial improvement for real-world applications.
        output += f"Constraints: {constraints}\n"


    output += f"Responding to prompt: {prompt}\n"

    #Simulate a response - Replace this with a proper language model call in a real application
    if "dogs" in prompt.lower():
        if examples and any("golden retriever" in ex.lower() for ex in examples):
            output += "I'll write about Golden Retrievers, their friendly nature, and their suitability as family pets."
        else:
            output += "I'll write about dogs in general, covering various breeds and their characteristics."
    elif "doctor" in prompt.lower():
        if constraints and "gender" in constraints and "female" in constraints["gender"]:
            output += "I'll describe a female doctor, highlighting the diversity within the medical profession."  
        else:
            output += "I'll describe a doctor, focusing on their professional responsibilities and expertise, avoiding gender or race stereotypes." #still needs improvement
    else:
        output += "I'll attempt to respond to the prompt as directly as possible."


    return output



# Example usage:

# Ambiguous prompt:
ambiguous_prompt = "Write about dogs"
ambiguous_output = generate_text(ambiguous_prompt)
print(f"Output for ambiguous prompt:\n{ambiguous_output}\n")



# Ambiguous prompt with examples to reduce ambiguity:
clearer_prompt = "Write about dogs"
examples_dogs = ["Golden Retrievers are known for their friendly demeanor.", "German Shepherds are intelligent and loyal."]
clearer_output = generate_text(clearer_prompt, examples=examples_dogs)
print(f"Output for clearer prompt with examples:\n{clearer_output}\n")


# Biased prompt with constraints:
biased_prompt = "Describe a typical doctor"
constrained_output = generate_text(biased_prompt, constraints={"gender": ["female"]})
print(f"Output for biased prompt with constraints:\n{constrained_output}\n")


# More complex prompt:

complex_prompt = "Write a story about a brave firefighter rescuing a cat"
complex_output = generate_text(complex_prompt)
print(f"Output for complex prompt:\n{complex_output}\n")


