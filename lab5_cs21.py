import random
import math

def generate_initial_state(n):
  """Generates a random initial state for the N-Queens problem."""
  return [random.randint(0, n - 1) for _ in range(n)]


def calculate_cost(state):
  """Calculates the number of conflicts in the current state."""
  n = len(state)
  cost = 0
  for i in range(n):
    for j in range(i + 1, n):
      if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
        cost += 1
  return cost


def get_neighbor(state):
  """Generates a neighboring state by moving a single queen to a different row."""
  n = len(state)
  new_state = list(state)
  queen_index = random.randint(0, n - 1)
  new_row = random.randint(0, n - 1)
  new_state[queen_index] = new_row
  return new_state


def simulated_annealing(n, initial_temperature, cooling_rate):
  """Solves the N-Queens problem using simulated annealing."""
  current_state = generate_initial_state(n)
  current_cost = calculate_cost(current_state)
  temperature = initial_temperature

  while temperature > 1:
    neighbor_state = get_neighbor(current_state)
    neighbor_cost = calculate_cost(neighbor_state)

    if neighbor_cost < current_cost:
      current_state = neighbor_state
      current_cost = neighbor_cost
    else:
      delta_cost = neighbor_cost - current_cost
      probability = math.exp(-delta_cost / temperature)
      if random.random() < probability:
        current_state = neighbor_state
        current_cost = neighbor_cost

    temperature *= cooling_rate

  return current_state, current_cost


# Example usage:
n = 8
initial_temperature = 100
cooling_rate = 0.95

solution, cost = simulated_annealing(n, initial_temperature, cooling_rate)

if cost == 0:
  print("Solution found:")
  print(solution)
else:
  print("Local minimum found with cost:", cost)
