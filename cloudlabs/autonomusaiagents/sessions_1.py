
# Introduction to Autonomous AI Agents: A Simple Example

# This program simulates a very basic autonomous agent that navigates a simple grid world.
# The agent's goal is to reach a target location.  It uses a simple rule-based approach,
# not sophisticated machine learning.  This is for illustrative purposes only.


# Define the grid world (0 = empty, 1 = obstacle, 2 = target)
grid = [
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 2],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]


# Agent's starting position
agent_x = 0
agent_y = 0


# Function to check if a move is valid
def is_valid_move(x, y):
    #Check boundaries
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
        return False
    #Check for obstacles
    if grid[x][y] == 1:
        return False
    return True


# Simple rule-based agent behavior: move towards the target
# (This could be replaced with more sophisticated algorithms)
def agent_move():
    global agent_x, agent_y
    target_x = 0
    target_y = 0

    #Find the target
    for i in range(len(grid)):
      for j in range(len(grid[i])):
        if grid[i][j] == 2:
          target_x = i
          target_y = j
          break
      else:
        continue
      break

    #Try to move closer to the target

    if agent_x < target_x and is_valid_move(agent_x + 1, agent_y):
        agent_x += 1
    elif agent_x > target_x and is_valid_move(agent_x - 1, agent_y):
        agent_x -= 1
    elif agent_y < target_y and is_valid_move(agent_x, agent_y + 1):
        agent_y += 1
    elif agent_y > target_y and is_valid_move(agent_x, agent_y - 1):
        agent_y -= 1


# Simulate the agent's actions
#The agent will keep moving until it reaches the target
while grid[agent_x][agent_y] != 2:
    print(f"Agent's position: ({agent_x}, {agent_y})")
    agent_move()

print(f"Agent reached the target at ({agent_x}, {agent_y})!")


