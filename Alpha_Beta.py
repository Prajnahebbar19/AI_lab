# Alpha-Beta Pruning Implementation
def alpha_beta_pruning(depth, node_index, maximizing_player, values, alpha, beta):
    # Base case: Leaf node
    if depth == 3:  # Assuming depth of 3 for the provided tree
        return values[node_index]
    if maximizing_player:
        max_eval = float('-inf')
        for i in range(2):  # Each node has 2 children
            eval_value = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, eval_value)
            alpha = max(alpha, eval_value)
            # Prune the branch
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(2):  # Each node has 2 children
            eval_value = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, eval_value)
            beta = min(beta, eval_value)
            # Prune the branch
            if beta <= alpha:
                break
        return min_eval
# Example Usage
if __name__ == "__main__":
    # Values at the leaf nodes of the game tree
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    alpha = float('-inf')
    beta = float('inf')
    result = alpha_beta_pruning(0, 0, True, values, alpha, beta)
    print("The optimal value is:", result)
