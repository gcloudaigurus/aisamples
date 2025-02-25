
import random

# This program demonstrates decision-making under uncertainty using a simple scenario:
# choosing between two investment options with uncertain returns.

# Define the possible returns for each investment option.  These are represented as dictionaries
# where keys are possible outcomes and values are their probabilities.
investment_A = {
    "high_return": 0.3,  # 30% chance of high return
    "medium_return": 0.5, # 50% chance of medium return
    "low_return": 0.2    # 20% chance of low return

}
investment_B = {
    "high_return": 0.2,  # 20% chance of high return
    "medium_return": 0.6, # 60% chance of medium return
    "low_return": 0.2    # 20% chance of low return
}

# Define the return values associated with each outcome.
returns = {
    "high_return": 1000,
    "medium_return": 500,
    "low_return": 100
}


def simulate_investment(investment_option):
    """Simulates the outcome of an investment option."""
    outcomes = list(investment_option.keys())
    probabilities = list(investment_option.values())
    outcome = random.choices(outcomes, weights=probabilities)[0]
    return returns[outcome]


def calculate_expected_value(investment_option):
    """Calculates the expected value of an investment option."""
    expected_value = 0
    for outcome, probability in investment_option.items():
        expected_value += probability * returns[outcome]
    return expected_value

#Simulate multiple runs to get a better sense of the distribution of returns.
num_simulations = 10000

A_returns = [simulate_investment(investment_A) for _ in range(num_simulations)]
B_returns = [simulate_investment(investment_B) for _ in range(num_simulations)]

# Calculate the average return for each investment over the simulations.
avg_A = sum(A_returns) / num_simulations
avg_B = sum(B_returns) / num_simulations

# Calculate the expected values of both investments.
expected_value_A = calculate_expected_value(investment_A)
expected_value_B = calculate_expected_value(investment_B)


print(f"Investment A: Average return from simulations: {avg_A:.2f}, Expected Value: {expected_value_A:.2f}")
print(f"Investment B: Average return from simulations: {avg_B:.2f}, Expected Value: {expected_value_B:.2f}")


#Decision making: A rational decision-maker would choose the investment with the higher expected value.
#In this example, this approach ignores risk aversion. A more sophisticated model might incorporate risk aversion
#using utility functions.  The simulation helps visualize the range of possible outcomes.


