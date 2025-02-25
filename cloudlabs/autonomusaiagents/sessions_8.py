
# This program simulates a simple robot navigating a grid world.
# The robot starts at (0,0) and aims to reach (3,3).
# It uses a simple A* search algorithm for path planning.

import heapq

# Define the grid world. 0 represents free space, 1 represents an obstacle.
grid = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0],
]

# Heuristic function (Manhattan distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* search algorithm
def a_star(grid, start, goal):
    open_set = [(0, start)]  # (f_score, (x, y))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        current_f, current = heapq.heappop(open_set)

        if current == goal:
            path = reconstruct_path(came_from, current)
            return path

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]: # Possible movements (up, right, down, left)
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and \
               grid[neighbor[0]][neighbor[1]] == 0: # Check for boundaries and obstacles
                tentative_g_score = g_score[current] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # No path found


# Reconstructs the path from the came_from dictionary
def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1] # Reverse the path to get it from start to goal


# Start and goal coordinates
start = (0, 0)
goal = (3, 3)

# Find the path
path = a_star(grid, start, goal)

# Print the path
if path:
    print("Path found:", path)
else:
    print("No path found.")


#Simulate robot movement (This part is a basic example and could be significantly expanded)
print("\nRobot Navigation Simulation:")
if path:
    for position in path:
        print(f"Robot moved to: {position}")


