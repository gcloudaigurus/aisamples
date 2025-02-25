
# Introduction to Prompt Engineering & LLMs: A Sample Program

# This program demonstrates basic prompt engineering concepts using a simple LLM-like function.
#  A real LLM would be much more complex and powerful,  but this provides a conceptual overview.


# Simulates a Large Language Model (LLM).  In reality, this would be replaced by an API call to a service like OpenAI, Cohere, etc.
def simple_llm(prompt):
    """
    This is a simplified LLM that responds to prompts based on simple keyword matching.
    It's not a true LLM, but it helps illustrate the prompt engineering process.
    """
    #  Note: Replace this with actual LLM interaction for a real-world application
    prompt = prompt.lower() # Convert the input to lowercase for case-insensitive matching
    if "hello" in prompt:
        return "Hello to you too!"
    elif "weather" in prompt:
        return "The weather is pleasant today."
    elif "goodbye" in prompt:
        return "Farewell!"
    else:
        return "I'm not sure I understand."


# Example of prompt engineering:  Different prompts to achieve different responses

prompt1 = "Hello, how are you?"  # Friendly greeting
response1 = simple_llm(prompt1)
print(f"Prompt: {prompt1}\nResponse: {response1}\n") #Example of output formatting


prompt2 = "What's the weather like?" # Specific question
response2 = simple_llm(prompt2)
print(f"Prompt: {prompt2}\nResponse: {response2}\n")


prompt3 = "goodbye cruel world" # Contains a keyword
response3 = simple_llm(prompt3)
print(f"Prompt: {prompt3}\nResponse: {response3}\n")


prompt4 = "Tell me a joke." # A prompt the simplified LLM cannot handle
response4 = simple_llm(prompt4)
print(f"Prompt: {prompt4}\nResponse: {response4}\n")


#Demonstrates the importance of clear and specific prompts for better results.
#Prompt Engineering involves crafting prompts to elicit desired responses from the LLM.
#This includes techniques like few-shot learning, chain-of-thought prompting, etc. (not shown here for simplicity).

#Further improvements could involve using a real LLM API, experimenting with different prompt formats, and analyzing the outputs.


