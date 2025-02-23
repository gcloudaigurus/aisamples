#This program demonstrates a simple Reinforcement Learning agent learning to navigate a small grid world using Q-learning.  It's a basic example, but showcases the core concepts.


import numpy as np
import random

# Define the grid world (0: empty, 1: wall, 2: goal)
grid = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 2]
])

# Actions: 0-up, 1-down, 2-left, 3-right
actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Q-table initialization (state, action) -> Q-value
q_table = np.zeros((grid.shape[0], grid.shape[1], len(actions)))

# Hyperparameters
learning_rate = 0.8
discount_factor = 0.95
exploration_rate = 0.1
num_episodes = 1000

def get_state(row, col):
    return row * grid.shape[1] + col

def get_next_state(row, col, action):
    new_row = row + actions[action][0]
    new_col = col + actions[action][1]

    # Check for boundaries and walls
    if (new_row < 0 or new_row >= grid.shape[0] or
            new_col < 0 or new_col >= grid.shape[1] or
            grid[new_row, new_col] == 1):
        return row, col
    else:
        return new_row, new_col


def get_reward(row, col):
    if grid[row, col] == 2:
        return 10  # Reward for reaching the goal
    else:
        return -1   # Penalty for each step


for episode in range(num_episodes):
    row, col = 0, 0  # Start at (0,0)
    done = False

    while not done:
        # Exploration vs. exploitation
        if random.uniform(0, 1) < exploration_rate:
            action = random.randint(0, len(actions) - 1)  # Explore randomly
        else:
            action = np.argmax(q_table[row, col])  # Exploit best Q-value

        next_row, next_col = get_next_state(row, col, action)
        reward = get_reward(next_row, next_col)
        done = (reward == 10) or (grid[next_row, next_col] == 1)


        # Q-learning update rule
        old_value = q_table[row, col, action]
        next_max = np.max(q_table[next_row, next_col])
        new_value = (1 - learning_rate) * old_value + learning_rate * (reward + discount_factor * next_max)
        q_table[row, col, action] = new_value

        row, col = next_row, next_col

print("Training complete.")

# Example of how to use the learned Q-table:
row, col = 0, 0
while grid[row, col] != 2:
    action = np.argmax(q_table[row, col])
    next_row, next_col = get_next_state(row, col, action)
    print(f"Going from ({row},{col}) to ({next_row},{next_col}) using action {action}")
    row, col = next_row, next_col

print("Reached the goal!")



#This code trains a Q-learning agent on a simple 3x3 grid. You can experiment by changing the `grid`, hyperparameters, and the reward structure to observe how the agent's learning behavior changes.  Remember that this is a very simplified example, and real-world RL problems are far more complex.  Libraries like OpenAI Gym provide more sophisticated environments for RL experimentation.
