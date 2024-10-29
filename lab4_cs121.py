
#Implement Hill Climbing search algorithm to solve N-Queens problem

import random

def is_safe(board, row, col, n):
  """Checks if it's safe to place a queen at the given position."""
  for i in range(row):
    if board[i] == col or \
       abs(board[i] - col) == row - i:
      return False
  return True

def calculate_heuristic(board, n):
  """Calculates the number of pairs of queens attacking each other."""
  heuristic_value = 0
  for i in range(n):
    for j in range(i + 1, n):
      if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
        heuristic_value += 1
  return heuristic_value

def hill_climbing_nqueens(n):
  """Solves the N-Queens problem using hill climbing."""
  current_board = [random.randint(0, n - 1) for _ in range(n)]
  current_heuristic = calculate_heuristic(current_board, n)

  while True:
    neighbors = []
    for row in range(n):
      for col in range(n):
        if current_board[row] != col:
          neighbor_board = current_board[:]
          neighbor_board[row] = col
          neighbors.append(neighbor_board)

    best_neighbor = None
    best_neighbor_heuristic = current_heuristic

    for neighbor in neighbors:
      neighbor_heuristic = calculate_heuristic(neighbor, n)
      if neighbor_heuristic < best_neighbor_heuristic:
        best_neighbor_heuristic = neighbor_heuristic
        best_neighbor = neighbor

    if best_neighbor is None:
      break  # No better neighbor found, local optima reached

    current_board = best_neighbor
    current_heuristic = best_neighbor_heuristic

  return current_board, current_heuristic


def print_board(board):
  n = len(board)
  for row in range(n):
    line = ""
    for col in range(n):
      if board[row] == col:
        line += "Q "
      else:
        line += ". "
    print(line)

# Example usage for 8-Queens
n = 8
solution, heuristic = hill_climbing_nqueens(n)

if heuristic == 0:
  print("Solution found:")
  print_board(solution)
else:
  print("Local optima reached, not a perfect solution.")
  print("Heuristic value:", heuristic)
  print_board(solution)
