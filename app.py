import random
import numpy as np
import functions as fn

# Fetch user's decision list
user_input = input("Enter decisions to make, separated by commas: ")
user_list = [s.strip() for s in user_input.split(",")]
random.shuffle(user_list)

# Initialize ranking matrix & Rank
n = len(user_list)
L = np.zeros((n, n))
weights = fn.decision_rank(L, 0.9)

while fn.check_if_tie(weights):
    # Take first two idices of the ties:
    idx1, idx2 = fn.get_tie_indices(weights)

    # Ask user to pick
    print("\n")
    print(f"A: {user_list[idx1]}")
    print(f"B: {user_list[idx2]}")
    picked = input("Please pick one: ").capitalize()

    if picked.capitalize() == "A":
        idx_p = idx1
        idx_np = idx2
    elif picked.capitalize() == "B":
        idx_p = idx2
        idx_np = idx1
    else:
        print("Please pick between A or B.")

    # Update the ranking matrix & Re-rank
    L[idx_p, idx_np] += 1
    weights = fn.decision_rank(L, 0.9)

final = fn.return_ranked_list(user_list, weights)

print("\nYour ranking:")
for i in range(len(final)):
    print(f"{i+1}. {final[i]}")
print("\n")
