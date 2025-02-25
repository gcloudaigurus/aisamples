
# Advanced Prompt Engineering Techniques: Demonstrating Few-Shot Learning and Chain-of-Thought Prompting

# Few-Shot Learning:  We'll provide a few examples within the prompt to guide the model's response.
# This helps the model understand the desired format and task without explicit instructions.

# Chain-of-Thought Prompting: We encourage the model to break down the problem into smaller, logical steps.
# This leads to more accurate and explainable reasoning, especially for complex tasks.


def few_shot_chain_of_thought_example(query):
    # Example demonstrating both techniques simultaneously.
    prompt = """
    Q: What is the capital of France?
    A: Paris

    Q: What is the largest planet in our solar system?
    A: Jupiter

    Q: If a train leaves Chicago at 8 am traveling at 60 mph and arrives in St. Louis at 2 pm, how far is it between the cities?
    A: To solve this, first we need to calculate the travel time: 2 pm - 8 am = 6 hours.
       Then, we multiply the speed by the time: 60 mph * 6 hours = 360 miles.
       Therefore, the distance between Chicago and St. Louis is 360 miles.


    Q: A farmer has 17 sheep. All but 9 die. How many are left?
    A: Let's think step by step.
       The problem states that all but 9 sheep died. 
       This means 9 sheep survived.
       Therefore, there are 9 sheep left.


    Q:  If a plane takes off at 10 am, flying at 500 mph, and reaches its destination in 3 hours, at what time does it reach its destination?

    A: """ + query + """
    """
    # In a real-world scenario, you would use a language model API here (e.g., OpenAI, Hugging Face).
    #  This placeholder simulates a model's response.  Replace this with your actual API call.

    # Simulating a language model response incorporating chain of thought
    if query == "What time does the plane reach its destination?":
        model_response = "The flight takes 3 hours.  10 am + 3 hours = 1 pm.  The plane reaches its destination at 1 pm."
    elif query == "What is the speed of light?":
        model_response = "Let's break this down: The speed of light is a fundamental constant in physics.  Its value is approximately 299,792,458 meters per second."
    else:
        model_response = "I cannot answer this question."


    return model_response


#Example Usage
query1 = "What time does the plane reach its destination?"
query2 = "What is the speed of light?"
query3 = "What is the meaning of life?"


print(f"Query: {query1}\nResponse: {few_shot_chain_of_thought_example(query1)}\n")
print(f"Query: {query2}\nResponse: {few_shot_chain_of_thought_example(query2)}\n")
print(f"Query: {query3}\nResponse: {few_shot_chain_of_thought_example(query3)}\n")


