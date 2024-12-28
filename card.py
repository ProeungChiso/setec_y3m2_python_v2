import random

num = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
suits = ("\u2663", "\u2666", "\u2665", "\u2660")

cards = []
for n in num:
    for s in suits:
        cards.append(n + s)

value_map = {
    "A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
    "8": 8, "9": 9, "10": 10, "J": 0, "Q": 0, "K": 0
}

num_players = int(input("Enter number of players: "))

random.shuffle(cards)
hands = {}
not_enough_cards = []

for i in range(num_players):
    if len(cards) >= 3:
        hand = []
        for _ in range(3):
            hand.append(cards.pop())
            hands[f"Player {i+1}"] = hand
    else:
        not_enough_cards.append(f"Player {i+1}")

if not_enough_cards:
    print("\nEnough Cards")
    for player in not_enough_cards:
        print(player)

scores = {}

for player, hand in hands.items():
    total = 0
    for card in hand:
        total += value_map[card[:-1]]
    score = total % 10
    scores[player] = score
    print(f"{player} has cards {hand} : {score}")

if scores:
    max_score = max(scores.values())
    winners = []
    
    for player, score in scores.items():
        if score == max_score:
            winners.append(player)

    print("\nWinner:")
    for winner in winners:
        print(winner)
