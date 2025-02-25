
# This program demonstrates a simple environment modeling and representation using a grid-based approach.
# It represents a 2D environment with obstacles and a goal.
# The environment is represented as a list of lists (a 2D array).

# Define the environment dimensions
grid_width = 10
grid_height = 10

# Create the grid, 0 represents free space, 1 represents an obstacle, and 2 represents the goal.
environment = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 2, 0], # Goal location (2)
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


# Function to print the environment grid
def print_environment(env):
    #Iterate through rows and print each cell
    for row in env:
        print(' '.join(map(str,row)))


# Function to check if a given position is valid (within bounds and not an obstacle)

def is_valid_position(row, col):
    #check if the position is within the bounds of the grid and not an obstacle.
    return 0 <= row < grid_height and 0 <= col < grid_width and environment[row][col] != 1


# Example usage: Print the environment
print("Environment Representation:")
print_environment(environment)

# Example usage: Check if a position is valid
row = 5
col = 8
if is_valid_position(row, col):
    print(f"\nPosition ({row}, {col}) is valid.")
else:
    print(f"\nPosition ({row}, {col}) is invalid.")

#Further development could include pathfinding algorithms (A*, Dijkstra's) to find a path from a starting point to the goal,
#agent simulation, and more sophisticated environment representations (e.g., using classes and objects).


