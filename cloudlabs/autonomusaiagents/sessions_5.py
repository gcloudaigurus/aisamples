
# This program simulates a simple multi-agent system where agents
# search for a target in a 2D grid world.

import random

# Define the agent class
class Agent:
    def __init__(self, x, y, id):
        # Initialize agent's position and ID
        self.x = x
        self.y = y
        self.id = id
        self.found_target = False

    def move(self, grid_size):
        # Agent randomly moves one step in a random direction
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])
        self.x = max(0, min(self.x + dx, grid_size -1)) # Keep agent within grid bounds
        self.y = max(0, min(self.y + dy, grid_size -1))

    def check_target(self, target_x, target_y):
        # Check if agent has found the target
        if self.x == target_x and self.y == target_y:
            self.found_target = True
            print(f"Agent {self.id} found the target!")


# Define the environment
grid_size = 10  # Size of the grid world
num_agents = 5  # Number of agents
target_x = 7
target_y = 3

# Initialize agents and target
agents = []
for i in range(num_agents):
    agents.append(Agent(random.randint(0, grid_size - 1), random.randint(0, grid_size - 1), i))

# Simulation loop
for step in range(100): # Simulate for a fixed number of steps
    print(f"Step {step + 1}:")
    for agent in agents:
        if not agent.found_target: #Only move if target not found
            agent.move(grid_size)
            agent.check_target(target_x, target_y)
            print(f"  Agent {agent.id}: Position ({agent.x}, {agent.y})")
    
    #Check if any agent found the target.  If so, break the loop.
    if any(agent.found_target for agent in agents):
      break


#Note: This is a very basic example.  A more sophisticated multi-agent system might include:
# -More complex agent behaviors (e.g., communication, cooperation, competition)
# -A more realistic environment (e.g., obstacles, dynamic targets)
# -Mechanisms for agent creation and destruction
# -Performance metrics to evaluate the system's effectiveness


