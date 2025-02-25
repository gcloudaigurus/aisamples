
# Import necessary libraries
import gym
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam

# Define the Deep Q-Network (DQN) agent
class DQNAgent:
    def __init__(self, state_size, action_size):
        # Initialize agent parameters
        self.state_size = state_size
        self.action_size = action_size
        self.memory = [] # Replay memory to store experiences
        self.gamma = 0.95  # Discount factor for future rewards
        self.epsilon = 1.0  # Exploration rate (initially explore fully)
        self.epsilon_min = 0.01  # Minimum exploration rate
        self.epsilon_decay = 0.995  # Rate at which exploration decays
        self.learning_rate = 0.001
        self.model = self._build_model() #Build the neural network model

    # Build the neural network model using TensorFlow/Keras
    def _build_model(self):
        model = Sequential()
        model.add(Flatten(input_shape=(self.state_size,))) #Flatten the input state
        model.add(Dense(24, activation='relu')) #Hidden layer with ReLU activation
        model.add(Dense(24, activation='relu')) #Another hidden layer
        model.add(Dense(self.action_size, activation='linear')) #Output layer with linear activation (for Q-values)
        model.compile(loss='mse', optimizer=Adam(learning_rate=self.learning_rate))
        return model

    # Store experience in replay memory
    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    # Choose an action using epsilon-greedy strategy
    def act(self, state):
        if np.random.rand() <= self.epsilon:
            # Explore: choose a random action
            return np.random.randint(self.action_size)
        else:
            # Exploit: choose action with highest Q-value
            act_values = self.model.predict(state)
            return np.argmax(act_values[0])  

    # Train the DQN model using replay memory
    def replay(self, batch_size):
        minibatch = np.random.choice(self.memory, batch_size, replace=False)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = reward + self.gamma * np.amax(self.model.predict(next_state)[0])
            target_f = self.model.predict(state)
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)  # Train the model
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    # Load weights from a file
    def load(self, name):
        self.model.load_weights(name)

    # Save weights to a file
    def save(self, name):
        self.model.save_weights(name)


# Main function to train and run the agent
if __name__ == "__main__":
    env = gym.make('CartPole-v1') #Use CartPole environment
    state_size = env.observation_space.shape[0] #Get state size from environment
    action_size = env.action_space.n #Get action size from environment
    agent = DQNAgent(state_size, action_size) #Create agent
    done = False
    batch_size = 32
    episodes = 1000 #Number of training episodes

    for e in range(episodes):
        state = env.reset() #Reset the environment at the start of each episode
        state = np.reshape(state, [1, state_size]) #Reshape state to match model input
        for time in range(500):  #Maximum time steps per episode
            env.render()  #Render environment (optional)
            action = agent.act(state) #Agent chooses action
            next_state, reward, done, _ = env.step(action) #Take action and get feedback from environment
            next_state = np.reshape(next_state, [1, state_size]) #Reshape next_state
            reward = reward if not done else -10 #Assign reward (penalize for failure)
            agent.remember(state, action, reward, next_state, done) #Store the experience
            state = next_state #Update state
            if done:
                print("episode: {}/{}, score: {}, e: {:.2}"
                      .format(e, episodes, time, agent.epsilon))
                break
            if len(agent.memory) > batch_size:
                agent.replay(batch_size) #Train the model using replay memory
    agent.save("cartpole-dqn.h5")  #Save the trained model weights
    env.close() #Close the environment
