
# This program demonstrates a simple planning and search algorithm: Breadth-First Search (BFS)
# It solves a basic puzzle of finding a path from a start state to a goal state.

# Define the states as tuples representing the arrangement of tiles.
# The goal state is predefined.

goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0) # 0 represents the empty tile

# Define actions as possible moves (up, down, left, right).  These modify the state.
def get_neighbors(state):
    neighbors = []
    index = state.index(0) # Find the empty tile's index
    row, col = divmod(index, 3) # Get row and column of empty tile

    #Possible moves and their effect on the index of the empty tile.
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Up, Down, Left, Right
    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3: # Check if move is within bounds
            new_index = new_row * 3 + new_col
            new_state = list(state)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append(tuple(new_state))
    return neighbors

# BFS algorithm implementation using a queue.
def bfs(start_state, goal_state):
    queue = [(start_state, [start_state])] # Queue of (state, path_so_far)
    visited = set()

    while queue:
        current_state, path = queue.pop(0)
        if current_state == goal_state:
            return path

        visited.add(current_state)
        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return None # No solution found


# Example usage:
start_state = (1, 2, 3, 4, 0, 6, 7, 5, 8) # Example start state

solution_path = bfs(start_state, goal_state)

if solution_path:
    print("Solution found:")
    for state in solution_path:
        print(state)
else:
    print("No solution found.")


