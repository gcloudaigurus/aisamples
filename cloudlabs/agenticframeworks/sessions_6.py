
# This program simulates a simple multi-agent system where agents communicate and collaborate to achieve a common goal.
# The goal is to collectively find the maximum value in a list distributed among the agents.

import random
import time

# Agent class
class Agent:
    def __init__(self, agent_id, data_slice):
        self.agent_id = agent_id
        self.data_slice = data_slice  # Agent's portion of the data
        self.max_value = max(data_slice) #Initial local maximum


    def communicate(self, other_agent):
        # Agents exchange their current maximum values.
        if self.max_value < other_agent.max_value:
            self.max_value = other_agent.max_value
        print(f"Agent {self.agent_id} received {other_agent.max_value} from Agent {other_agent.agent_id}")


    def collaborate(self, other_agent):
        #Simulate collaboration - agents update max value after communication.  This could be more complex in real applications.
        self.communicate(other_agent)
        other_agent.communicate(self)



# Data initialization
data = list(range(100))
random.shuffle(data)

# Number of agents
num_agents = 4

# Distribute data among agents
data_slices = [data[i::num_agents] for i in range(num_agents)]

# Create agents
agents = [Agent(i, data_slices[i]) for i in range(num_agents)]

# Communication and collaboration phase
print("Initial local maximums:")
for agent in agents:
    print(f"Agent {agent.agent_id}: {agent.max_value}")
time.sleep(1) #Simulate some time passing between communication rounds


#Round 1 of communication and collaboration
agents[0].collaborate(agents[1])
time.sleep(1)
agents[2].collaborate(agents[3])
time.sleep(1)

#Round 2 of communication and collaboration (agents need to communicate across groups)
agents[0].collaborate(agents[2])
time.sleep(1)


#Results
print("\nFinal maximum values after collaboration:")
for agent in agents:
    print(f"Agent {agent.agent_id}: {agent.max_value}")

#Finding the overall maximum value across all agents.  This could be handled more efficiently in a large system.
overall_max = 0
for agent in agents:
    if agent.max_value > overall_max:
        overall_max = agent.max_value

print(f"\nThe overall maximum value is: {overall_max}")


