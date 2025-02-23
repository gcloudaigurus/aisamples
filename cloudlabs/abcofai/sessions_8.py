#This program demonstrates a simple AI-powered robotic arm simulation using Pygame. It utilizes a basic Q-learning algorithm to learn how to reach a target position.  Because a real robotic arm is not involved, this is a simplified simulation, but it captures core principles of AI in robotics.



import pygame
import random
import numpy as np

# Initialize Pygame
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("AI Robotic Arm Simulation")

# Arm parameters
arm_length = 100
arm_segments = 2
joint_angles = [0, 0]  # Initial angles (radians)

# Target position
target_x = 400
target_y = 300

# Q-learning parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration rate
q_table = {}

# Discretize the state and action space
num_states = 10  # Number of discrete positions for each joint angle
num_actions = 3   # Actions: -1 (decrease angle), 0 (no change), 1 (increase angle)
state_bins = np.linspace(-np.pi, np.pi, num_states + 1)
action_bins = [-1, 0, 1]


def get_state():
    """Discretizes the joint angles into a state."""
    state_index = [np.digitize(angle, state_bins) -1 for angle in joint_angles]
    return tuple(state_index)


def get_reward(x, y):
    """Calculates the reward based on distance to target."""
    distance = np.sqrt((x - target_x)**2 + (y - target_y)**2)
    reward = -distance  # Closer to target = higher reward
    return reward


def update_q_table(state, action, reward, next_state):
  """Updates the Q-table using the Q-learning algorithm."""
  if state not in q_table:
      q_table[state] = [0] * num_actions
  if next_state not in q_table:
      q_table[next_state] = [0] * num_actions

  q_table[state][action] = q_table[state][action] + alpha * (reward + gamma * np.max(q_table[next_state]) - q_table[state][action])


def choose_action(state):
  """Chooses an action using epsilon-greedy strategy."""
  if random.uniform(0, 1) < epsilon:
      return random.randint(0, num_actions - 1) # Explore
  else:
      return np.argmax(q_table[state]) # Exploit


def update_arm_position(action_index):
    """Update the arm joint angles."""
    angle_change = action_bins[action_index] * 0.1 #small angle increments
    joint_angles[0] += angle_change
    joint_angles[1] += angle_change
    joint_angles = [max(-np.pi, min(np.pi, angle)) for angle in joint_angles] # constraint angles within -pi to +pi

def draw_arm():
    """Draws the robotic arm on the screen."""
    x1 = screen_width // 2
    y1 = screen_height // 2
    x2 = x1 + arm_length * np.cos(joint_angles[0])
    y2 = y1 + arm_length * np.sin(joint_angles[0])
    x3 = x2 + arm_length * np.cos(joint_angles[0] + joint_angles[1])
    y3 = y2 + arm_length * np.sin(joint_angles[0] + joint_angles[1])


    pygame.draw.line(screen, (255, 0, 0), (x1, y1), (x2, y2), 5)
    pygame.draw.line(screen, (0, 255, 0), (x2, y2), (x3, y3), 5)
    pygame.draw.circle(screen, (0, 0, 255), (target_x, target_y), 10)

    return x3, y3 #end effector position

#Main loop
running = True
for i in range(10000):
    state = get_state()
    action = choose_action(state)
    update_arm_position(action)
    x, y = draw_arm()
    reward = get_reward(x, y)
    next_state = get_state()
    update_q_table(state, action, reward, next_state)

    screen.fill((0, 0, 0)) #clear screen
    draw_arm()
    pygame.display.flip()
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

#To run this code, you will need to have Pygame installed (`pip install pygame`).  Remember this is a very basic simulation;  a real-world robotics application would involve much more complex modelling, sensor integration, and control algorithms.  This example provides a starting point for understanding how reinforcement learning can be applied to robotic control.
