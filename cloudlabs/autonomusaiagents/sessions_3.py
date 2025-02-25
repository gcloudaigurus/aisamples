
import numpy as np
import random

# Define the environment
# A simple grid world with 4 states (0, 1, 2, 3) and 4 actions (0: up, 1: down, 2: left, 3: right)
# State 3 is the goal state, and state 0 is the starting state.

class GridWorld:
    def __init__(self):
        self.state = 0  #Initial state
        self.goal_state = 3

    def step(self, action):
        #Transition dynamics
        if self.state == 0:
            if action == 0: self.state = 0 #cannot move up from 0
            elif action == 1: self.state = 1
            elif action == 2: self.state = 0 #cannot move left from 0
            elif action == 3: self.state = 0 #cannot move right from 0

        elif self.state == 1:
            if action == 0: self.state = 0
            elif action == 1: self.state = 1 #cannot move down from 1
            elif action == 2: self.state = 0
            elif action == 3: self.state = 2

        elif self.state == 2:
            if action == 0: self.state = 1
            elif action == 1: self.state = 3
            elif action == 2: self.state = 2 #cannot move left from 2
            elif action == 3: self.state = 2 #cannot move right from 2

        elif self.state == 3: #Goal state
            pass # No state transition from goal state.
            

        reward = 1 if self.state == self.goal_state else 0 # reward only at goal
        done = self.state == self.goal_state # Episode ends when goal is reached.

        return self.state, reward, done


# Q-learning algorithm
# Simple Q-learning implementation with a fixed learning rate and discount factor.

def q_learning(env, num_episodes, alpha=0.1, gamma=0.9, epsilon=0.1):
    # Initialize Q-table (state-action value function)
    q_table = np.zeros((4, 4)) # 4 states, 4 actions

    for episode in range(num_episodes):
        state = env.state #Reset to initial state at beginning of each episode
        done = False
        while not done:
            # Epsilon-greedy action selection
            if random.uniform(0, 1) < epsilon:
                action = env.step(random.randint(0,3))
            else:
                action = np.argmax(q_table[state])

            next_state, reward, done = env.step(action)  

            # Q-learning update rule
            q_table[state, action] = q_table[state, action] + alpha * (reward + gamma * np.max(q_table[next_state]) - q_table[state, action])

            state = next_state

    return q_table



# Run the Q-learning algorithm and print the learned Q-table
env = GridWorld()
q_table = q_learning(env, num_episodes=1000)
print(q_table)


