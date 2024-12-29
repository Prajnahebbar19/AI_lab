import heapq
# Define the goal state
GOAL_STATE = [[1, 2, 3],
              [8, 0, 4],
              [7, 6, 5]]

# Utility function to find the position of the blank tile
def find_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def h(state):
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != GOAL_STATE[i][j]:
                misplaced += 1
    return misplaced

# Generate possible moves (Up, Down, Left, Right)
def get_neighbors(state):
    neighbors = []
    x, y = find_blank_position(state)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# A* search algorithm
def a_star_search(initial_state):
    open_list = []
    heapq.heappush(open_list, (h(initial_state), 0, initial_state, []))  # (f(n), g(n), state, path)
    closed_set = set()
    while open_list:
        f, g, current_state, path = heapq.heappop(open_list)
        if current_state == GOAL_STATE:
            return path + [current_state]  # Return the path to the goal
        closed_set.add(tuple(tuple(row) for row in current_state))  # Add to closed set
        for neighbor in get_neighbors(current_state):
            neighbor_tuple = tuple(tuple(row) for row in neighbor)
            if neighbor_tuple in closed_set:
                continue
            heapq.heappush(open_list, (g + 1 + h(neighbor), g + 1, neighbor, path + [current_state]))
    return None  # No solution

# Print the puzzle state
def print_state(state):
    for row in state:
        print(row)
    print()

# Define the initial state
initial_state = [[2, 8, 3],
                 [1, 6, 4],
                 [0, 7, 5]]

# Run the A* search
solution_path = a_star_search(initial_state)
# Print the solution path
if solution_path:
    print("Solution found in", len(solution_path)-1, "moves:")
    for step in solution_path:
        print_state(step)
else:
    print("No solution found.")
# Heuristic function: Manhattan distance
import heapq
# Define the goal state
GOAL_STATE = [[1, 2, 3],
              [8, 0, 4],
              [7, 6, 5]]
# Utility function to find the position of the blank tile
def find_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
def h(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_x, goal_y = divmod(state[i][j] - 1, 3)
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance
# Generate possible moves (Up, Down, Left, Right)
def get_neighbors(state):
    neighbors = []
    x, y = find_blank_position(state)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)
    return neighbors
# A* search algorithm
def a_star_search(initial_state):
    open_list = []
    heapq.heappush(open_list, (h(initial_state), 0, initial_state, []))  # (f(n), g(n), state, path)
    closed_set = set()
    while open_list:
        f, g, current_state, path = heapq.heappop(open_list)
        if current_state == GOAL_STATE:
            return path + [current_state]  # Return the path to the goal
        closed_set.add(tuple(tuple(row) for row in current_state))  # Add to closed set
        for neighbor in get_neighbors(current_state):
            neighbor_tuple = tuple(tuple(row) for row in neighbor)
            if neighbor_tuple in closed_set:
                continue
            heapq.heappush(open_list, (g + 1 + h(neighbor), g + 1, neighbor, path + [current_state]))
    return None  # No solution


# Print the puzzle state
def print_state(state):
    for row in state:
        print(row)
    print()
# Define the initial state
initial_state = [[2, 8, 3],
                 [1, 6, 4],
                 [0, 7, 5]]
# Run the A* search
solution_path = a_star_search(initial_state)
# Print the solution path
if solution_path:
    print("Solution found in", len(solution_path)-1, "moves:")
    for step in solution_path:
        print_state(step)
else:
    print("No solution found.")
