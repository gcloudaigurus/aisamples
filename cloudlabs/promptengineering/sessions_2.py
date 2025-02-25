
# This program demonstrates crafting effective prompts by showing examples of good and bad prompts.
# It focuses on clarity, specificity, and avoiding ambiguity.

# Example 1: A poorly crafted prompt.  Too vague and open-ended.
bad_prompt1 = "Write something."  

# Example 2: A slightly better prompt, but still lacks specificity.
bad_prompt2 = "Write a story."

# Example 3: A more specific and effective prompt.  Provides context and constraints.
good_prompt1 = "Write a short story (around 200 words) about a cat who discovers a hidden portal in their backyard."

# Example 4: An even more effective prompt.  Specifies genre, tone, and target audience.
good_prompt2 = "Write a humorous short story (around 200 words) for children aged 6-8, about a cat who discovers a hidden portal in their backyard that leads to a land made of cheese."


#  Function to simulate a response to a prompt (replace with a more sophisticated model in a real application).
def generate_response(prompt):
    """Simulates a response to a given prompt.  In reality, this would involve a language model."""
    if "cat" in prompt.lower() and "portal" in prompt.lower():
        return "The cat, Whiskers, peered through the shimmering portal, its cheesy aroma wafting towards him..."
    elif "story" in prompt.lower():
        return "Once upon a time..."
    else:
        return "I need more information to write something."


#Testing the prompts
print("Response to bad_prompt1:", generate_response(bad_prompt1)) # Expected:  Generic or unhelpful response
print("Response to bad_prompt2:", generate_response(bad_prompt2)) # Expected: Generic or unhelpful response
print("Response to good_prompt1:", generate_response(good_prompt1)) # Expected: More specific response related to cats and portals
print("Response to good_prompt2:", generate_response(good_prompt2)) # Expected:  Even more specific and tailored response.


#This illustrates how clear and specific prompts lead to better, more relevant outputs.  
#In real-world applications, you'd replace the `generate_response` function with a call to a language model API.


