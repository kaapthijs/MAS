import numpy as np

num_iterations = 2000

# Matrix
payoffs = np.array([
    [(1, 5), (2, 2), (3, 4), (3, 1)],
    [(3, 0), (4, 1), (2, 5), (4, 2)],
    [(1, 3), (2, 6), (5, 2), (2, 3)]
])

# Initialize count of actions for both players
count_actions_p1 = np.zeros(3)  # Player 1 can choose between A, B, and C
count_actions_p2 = np.zeros(4)  # Player 2 can choose between W, X, Y, and Z


# Function that calculates the best response given opponent's actions
def best_response(payoffs, empirical_dist, player):
    if player == 1:
        # Player 1 is the row player
        expected_payoffs = np.dot(payoffs[:, :, 1], empirical_dist)
    else:
        # Player 2 is the column player
        expected_payoffs = np.dot(empirical_dist, payoffs[:, :, 0])
    best_responses = np.argwhere(expected_payoffs == np.amax(expected_payoffs)).flatten()
    return np.random.choice(best_responses)


# Runs the fictitious play algorithm
for i in range(num_iterations):
    # Calculates distributions
    empirical_dist_p1 = count_actions_p1 / (i + 1) if i > 0 else np.full(3, 1 / 3)  # Uniform distribution for start
    empirical_dist_p2 = count_actions_p2 / (i + 1) if i > 0 else np.full(4, 1 / 4)  # Uniform distribution for start

    # Players best respond to the current distribution of the opponent's actions
    action_p1 = best_response(payoffs, empirical_dist_p2, player=1)
    action_p2 = best_response(payoffs, empirical_dist_p1, player=2)

    # Updates action counts
    count_actions_p1[action_p1] += 1
    count_actions_p2[action_p2] += 1

# Calculates the average strategy for both players
mixed_strategy_p1 = count_actions_p1 / num_iterations
mixed_strategy_p2 = count_actions_p2 / num_iterations

# Prints results
print(mixed_strategy_p1, mixed_strategy_p2)
