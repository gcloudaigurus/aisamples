
# Building a Simple Agentic System

# This program simulates a simple agent interacting with its environment.
# The agent's goal is to find a "target" in a grid-based world.

# The environment is represented by a 2D list.
# 0 represents an empty space, 1 represents the agent, and 2 represents the target.

# The agent has a simple behavior: it moves randomly until it finds the target.


import random

# Define the environment size
grid_size = 5

# Initialize the environment
environment = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

# Place the agent and target randomly
agent_x, agent_y = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
target_x, target_y = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)

# Ensure agent and target are not in the same position.  Relocate if needed.
while agent_x == target_x and agent_y == target_y:
    target_x, target_y = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)


environment[agent_x][agent_y] = 1
environment[target_x][target_y] = 2

# Simulate the agent's actions
found_target = False
steps = 0

while not found_target:
    #Print the current state of the environment
    for row in environment:
        print(row)
    print("-"*10)

    # Agent moves randomly
    possible_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
    dx, dy = random.choice(possible_moves)
    new_x, new_y = agent_x + dx, agent_y + dy

    # Check boundaries
    if 0 <= new_x < grid_size and 0 <= new_y < grid_size:
        environment[agent_x][agent_y] = 0  # Clear the agent's previous position
        agent_x, agent_y = new_x, new_y
        environment[agent_x][agent_y] = 1  # Update the agent's new position

    # Check if the agent found the target
    if agent_x == target_x and agent_y == target_y:
        found_target = True
        print("Agent found the target!")
    steps += 1

print(f"It took the agent {steps} steps to find the target.")


