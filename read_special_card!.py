import math

# Special permutations of "JQK"
special_permutations = [
    "JQK", "JKQ", "QJK", "QKJ", "KJQ", "KQJ"
]

# Example hand to check
hand = ["J♠", "Q♥", "K♦"]

# Extract ranks from the hand (ignoring the suit)
values = sorted(card[:-1] for card in hand)  # Extract card ranks and sort
joined_values = "".join(values)  # Combine into a string like "JQK"

# Check if the hand matches any permutation of JQK
if joined_values in special_permutations:
    print("This hand matches a JQK permutation!")
else:
    print("This hand does not match a JQK permutation.")

# Probability calculation
# Total number of ways to choose 3 cards from 52
total_hands = math.comb(52, 3)

# Number of valid hands (JQK permutations)
valid_hands = 4 * 4 * 4  # 4 Jacks, 4 Queens, 4 Kings

# Probability of getting a special JQK hand
probability = valid_hands / total_hands

# Print the probability
print(f"The probability of drawing a special 'JQK' hand is: {probability:.6f}")
