
# Case Study 1: Simple Agent-Based Model for Sheep Herding

import random

# Define the Agent class
class Sheep:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        # Random movement within a bounded area.  Simple agent behavior.
        dx = random.randint(-1, 1)
        dy = random.randint(-1, 1)
        self.x = max(0, min(self.x + dx, 99)) #Keep sheep within a 100x100 area
        self.y = max(0, min(self.y + dy, 99))

class Shepherd:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def herd(self, sheep):
        #Shepherd attempts to move closer to the sheep's centroid
        centroid_x = sum([s.x for s in sheep]) / len(sheep)
        centroid_y = sum([s.y for s in sheep]) / len(sheep)

        dx = int((centroid_x - self.x) / 2) #Proportional movement towards centroid
        dy = int((centroid_y - self.y) / 2)
        self.x = max(0, min(self.x + dx, 99))
        self.y = max(0, min(self.y + dy, 99))

# Initialize the environment
sheep = [Sheep(random.randint(0, 99), random.randint(0, 99)) for _ in range(20)] #20 sheep
shepherd = Shepherd(50, 50) # Shepherd starts in the center

# Simulate the system for a number of steps
for _ in range(100): #Simulate 100 steps
    for s in sheep:
        s.move()
    shepherd.herd(sheep)

    # (Optional) Print the positions for visualization (example)
    #print(f"Shepherd: ({shepherd.x}, {shepherd.y})")
    #for i, s in enumerate(sheep):
        #print(f"Sheep {i+1}: ({s.x}, {s.y})")


# Case Study 2:  Simple bidding agent in an auction (Illustrative)

# This is a highly simplified example and does not represent a complete auction system

class BiddingAgent:
    def __init__(self, max_bid):
        self.max_bid = max_bid
        self.current_bid = 0

    def bid(self, current_highest_bid):
        #Simple strategy: bid slightly higher than the current highest bid, up to max.
        if current_highest_bid < self.max_bid:
            self.current_bid = current_highest_bid + 1
            return self.current_bid
        else:
            return 0 #don't bid

#Example usage
agent1 = BiddingAgent(10)
agent2 = BiddingAgent(15)
highest_bid = 0

#Simple auction simulation (Illustrative only)
highest_bid = agent1.bid(highest_bid)
highest_bid = agent2.bid(highest_bid)
print(f"Final highest bid: {highest_bid}") #Illustrative output

#Note: Real world agent-based models for auctions would require far more complex agent strategies and market mechanics.


#Further Case Studies could include:
# * Traffic flow simulation (cars as agents)
# * Predator-prey models (animals as agents)
# * Opinion dynamics (people as agents)
# * Market simulation (buyers and sellers as agents)

#These examples are simplified illustrations.  Real-world applications often involve more sophisticated agent architectures, interaction rules, and data analysis.

