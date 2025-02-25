
import random

# Goal Setting and Planning in Agentic Systems: A Simple Example

# This program simulates a simple agent trying to reach a goal location.
# The agent uses a rudimentary planning mechanism based on random movement.
# It demonstrates basic concepts of goal-setting and planning in an agential system.

# Define the environment (a 2D grid)
grid_size = 10
environment = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

# Define the agent's starting position
agent_x = 0
agent_y = 0

# Define the goal location
goal_x = 9
goal_y = 9

# Set a maximum number of steps for the agent
max_steps = 100

# Function to check if the agent has reached the goal
def is_goal_reached(x, y):
    return x == goal_x and y == goal_y

# Function to perform a planning step (random movement in this case)
def plan_step(x, y):
    possible_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)] # Up, Down, Right, Left
    dx, dy = random.choice(possible_moves)
    new_x = max(0, min(x + dx, grid_size -1)) #Keep within bounds
    new_y = max(0, min(y + dy, grid_size -1)) #Keep within bounds
    return new_x, new_y


# Main loop: The agent takes steps until it reaches the goal or the max steps are exceeded
steps_taken = 0
while not is_goal_reached(agent_x, agent_y) and steps_taken < max_steps:
    # Goal: Reach (goal_x, goal_y)
    # Planning: Choose a random move
    agent_x, agent_y = plan_step(agent_x, agent_y)
    steps_taken += 1
    print(f"Step {steps_taken}: Agent at ({agent_x}, {agent_y})")


# Check the outcome
if is_goal_reached(agent_x, agent_y):
    print("Goal reached!")
else:
    print("Goal not reached within the maximum number of steps.")


