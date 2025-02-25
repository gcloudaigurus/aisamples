
# Introduction to Agentic Frameworks: A Simple Example

# This program demonstrates a basic agentic framework using a simple agent 
# that interacts with a simulated environment.  An agentic framework focuses 
# on defining agents with their own perceptions, goals, and actions within 
# a specific environment.  This contrasts with purely reactive systems that 
# simply respond to stimuli without internal state or goals.

# Here, our agent is a simple "food-seeking" agent in a 2D grid world.

# Defining the environment
environment = [
    ["empty", "empty", "food"],
    ["empty", "empty", "empty"],
    ["empty", "food", "empty"]
]

# Defining the agent
class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hunger = 10  # Initial hunger level

    def perceive(self, env):
        # Simple perception: check for food in adjacent cells
        food_nearby = False
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]: #check up,down,right,left
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < len(env) and 0 <= ny < len(env[0]) and env[nx][ny] == "food":
                food_nearby = True
                break
        return food_nearby

    def decide(self, food_nearby):
        # Simple decision-making: move towards food if found, otherwise wander
        if food_nearby:
            return "move_towards_food"
        else:
            return "wander"


    def act(self, action, env):
        if action == "move_towards_food":
            #Simplified food seeking - just moves randomly if food nearby
            import random
            dx, dy = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
            self.x += dx
            self.y += dy
            self.hunger -=2 #Reduce hunger if moving towards food
            print("Agent moved towards potential food")

        elif action == "wander":
            import random
            dx, dy = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
            self.x += dx
            self.y += dy
            self.hunger -=1 #Reduce hunger while wandering
            print("Agent wandered")

        #Check boundaries
        self.x = max(0, min(self.x, len(env)-1))
        self.y = max(0, min(self.y, len(env[0])-1))

        #Check for food
        if env[self.x][self.y] == "food":
            print("Agent found food!")
            env[self.x][self.y] = "empty"
            self.hunger = 10 #Resets hunger


# Creating and running the agent
agent = Agent(0, 0) #Agent starts at (0,0)


#Simulation loop
for i in range(10): #Simulate for 10 turns
    food_nearby = agent.perceive(environment)
    action = agent.decide(food_nearby)
    agent.act(action, environment)
    print(f"Hunger level: {agent.hunger}")
    if agent.hunger <=0:
        print("Agent Starved!")
        break

#Note: This is a very rudimentary example.  Real-world agentic frameworks can 
#be significantly more complex, involving sophisticated perception, planning, 
#learning, and interaction with other agents.  They are often used in areas 
#like robotics, game AI, and multi-agent systems.

