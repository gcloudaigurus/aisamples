
# Import necessary libraries
import random

# Define a dictionary of greetings
greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!"]

# Define a dictionary of responses
responses = {
    "what's your name?": ["I'm a simple chatbot.", "I don't have a name."],
    "how are you?": ["I'm doing well, thank you!", "I'm fine, how about you?"],
    "what time is it?": ["I'm not sure, I don't have access to real-time information."],
    "goodbye": ["Goodbye!", "See you later!", "Bye!"]
}

# Define a function to get a random greeting
def get_greeting():
    return random.choice(greetings)

# Define a function to get a response
def get_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    
    # Check if the user input is in the responses dictionary
    if user_input in responses:
        # Return a random response from the list of responses
        return random.choice(responses[user_input])
    else:
        # Return a default response if the user input is not found
        return "I'm sorry, I don't understand."

# Define the main function
def main():
    # Print a greeting
    print(get_greeting())

    # Start the conversation loop
    while True:
        # Get user input
        user_input = input("You: ")

        # Check if the user wants to quit
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break

        # Get a response and print it
        response = get_response(user_input)
        print("Chatbot:", response)

# Run the main function
if __name__ == "__main__":
    main()


