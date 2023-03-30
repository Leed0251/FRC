import math


# rounding function
def round_up(amount, roundto):
    return int(math.ceil(amount / roundto)) * roundto


# Main Routine starts here
to_round = [2.75, 2.25, 2]

for item in to_round:
    rounded = round_up(item, 0.5)
    print(f"${item:.2f} --> ${rounded:.2f}")