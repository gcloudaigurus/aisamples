
import numpy as np
import random

# This program demonstrates a simple reinforcement learning agent learning to navigate a grid world.

# Define the grid world: 0 represents an empty space, 1 represents a wall, and 2 represents the goal.
grid_world = np.array([
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 2],
    [1, 1, 0, 0]
])

# Define actions: 0 = up, 1 = down, 2 = left, 3 = right
actions = [0, 1, 2, 3]

# Initialize Q-table (state-action values).  Rows represent states (grid positions), columns represent actions.
# We'll use a simple encoding: row * grid_width + col.
q_table = np.zeros((grid_world.shape[0] * grid_world.shape[1], len(actions)))

# Hyperparameters
learning_rate = 0.1
discount_factor = 0.9
exploration_rate = 0.1  # Probability of choosing a random action instead of the best action
num_episodes = 1000

# Function to get the state from row and column
def get_state(row, col):
    return row * grid_world.shape[1] + col

# Function to get the next state and reward after taking an action.
def take_action(state, action):
    row = state // grid_world.shape[1]
    col = state % grid_world.shape[1]
    
    if action == 0:  # Up
        new_row = max(0, row - 1)
        new_col = col
    elif action == 1:  # Down
        new_row = min(grid_world.shape[0] - 1, row + 1)
        new_col = col
    elif action == 2:  # Left
        new_row = row
        new_col = max(0, col - 1)
    elif action == 3:  # Right
        new_row = row
        new_col = min(grid_world.shape[1] - 1, col + 1)
    else:
        return state, 0 #invalid action

    if grid_world[new_row, new_col] == 1: # Hit a wall
        return state, -1 # Penalty for hitting a wall
    elif grid_world[new_row, new_col] == 2: # Reached the goal
        return get_state(new_row, new_col), 100 #Large reward for reaching goal
    else:
        return get_state(new_row, new_col), 0 #No reward for moving to empty space

# Q-learning algorithm
for episode in range(num_episodes):
    state = get_state(0,0) # Start at top-left corner
    done = False
    while not done:
        if random.uniform(0, 1) < exploration_rate:
            action = random.choice(actions) # Explore: choose a random action
        else:
            action = np.argmax(q_table[state, :])  # Exploit: choose the action with the highest Q-value

        next_state, reward = take_action(state, action)
        
        # Q-learning update rule
        q_table[state, action] = q_table[state, action] + learning_rate * (reward + discount_factor * np.max(q_table[next_state, :]) - q_table[state, action])
        
        state = next_state
        if reward == 100:
            done = True

# Print the learned Q-table (optional)
print(q_table)

#Example of using the learned Q-table to find a path (optional)
current_state = get_state(0,0)
path = [current_state]
while grid_world[current_state // grid_world.shape[1], current_state % grid_world.shape[1]] != 2:
    best_action = np.argmax(q_table[current_state])
    next_state, _ = take_action(current_state, best_action)
    path.append(next_state)
    current_state = next_state

print("Optimal path:", path)



