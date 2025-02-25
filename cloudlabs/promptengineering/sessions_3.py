
# Prompt Engineering Techniques: Part 1 -  Focusing on Clarity and Specificity

# This program demonstrates basic prompt engineering principles by 
# generating different responses based on variations in prompt clarity.

def generate_response(prompt, model="Simple Model"): #Simulates a language model
    """Simulates a language model generating a response based on the prompt."""
    #In a real scenario, this would call an actual language model API.
    
    if model == "Simple Model":
        if "summary" in prompt.lower():
            return "Here's a short summary:"
        elif "explain" in prompt.lower():
            return "Here's an explanation:"
        elif "list" in prompt.lower():
            return "Here's a list:"
        else:
            return "I need more information."

    #Add more sophisticated model simulations here if needed.


# Example 1: Vague Prompt
vague_prompt = "Tell me about dogs."
vague_response = generate_response(vague_prompt)
print(f"Vague Prompt: {vague_prompt}\nResponse: {vague_response}\n") # Notice the unspecific response


# Example 2: Specific Prompt - requesting a summary
specific_prompt_summary = "Give me a summary of the history of dogs."
specific_response_summary = generate_response(specific_prompt_summary)
print(f"Specific Prompt (Summary): {specific_prompt_summary}\nResponse: {specific_response_summary}\n") #More focused response


# Example 3: Specific Prompt - requesting explanation
specific_prompt_explain = "Explain the difference between dog breeds."
specific_response_explain = generate_response(specific_prompt_explain)
print(f"Specific Prompt (Explain): {specific_prompt_explain}\nResponse: {specific_response_explain}\n") # Targeted response


# Example 4: Specific Prompt - requesting a list
specific_prompt_list = "List five popular dog breeds."
specific_response_list = generate_response(specific_prompt_list)
print(f"Specific Prompt (List): {specific_prompt_list}\nResponse: {specific_response_list}\n") #Structured response


#Example 5:  Illustrating the impact of keywords

keyword_rich_prompt = "Summarize the key plot points of Hamlet and list three main characters."
keyword_poor_prompt = "Tell me about Hamlet."

keyword_rich_response = generate_response(keyword_rich_prompt)
keyword_poor_response = generate_response(keyword_poor_prompt)

print(f"Keyword Rich Prompt: {keyword_rich_prompt}\nResponse: {keyword_rich_response}\n")
print(f"Keyword Poor Prompt: {keyword_poor_prompt}\nResponse: {keyword_poor_response}\n") #Shows how keywords guide the response



#Further improvements could include:
# - More sophisticated model simulation to handle more complex prompts
# -  Adding examples of constraints (length, format, style) in prompts.
# - Implementing techniques to handle ambiguous queries.


