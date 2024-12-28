import random
from colorama import Fore, Back, Style

num = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
suits = ("\u2663", "\u2666", "\u2665", "\u2660")

special_cards = ["111", "222", "333", "444", "555", "666", "777", "888", "999", "101010", "JJJ", "QQQ", "KKK", "AAA"]
special_permutations = ["JQK", "JKQ", "QJK", "QKJ", "KJQ", "KQJ"]

cards = [n + s for n in num for s in suits]

value_map = {
    "A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
    "8": 8, "9": 9, "10": 10, "J": 0, "Q": 0, "K": 0
}

print("\nOriginal Card : ", len(cards))

num_players = int(input(f"\nEnter number of players: "))

random.shuffle(cards)
hands = {
    'Player 1': ['A♥', 'A♣', 'A♠'], 
    'Player 2': ['Q♥', 'K♥', 'J♠']}

if num_players == 2:
    num_players = 2

for i in range(num_players - 2):
    hands[f"Player {i+3}"] = [cards.pop() for _ in range(3)]

scores = {}
special_matches = {}

print(f"{Style.RESET_ALL}")
for player, hand in hands.items():
    print(f"{player} has cards {hand}")
    values = sorted(card[:-1] for card in hand)

    if values == ["1", "1", "1"]:
        special_matches[player] = "111"
    elif values == ["2", "2", "2"]:
        special_matches[player] = "222"
    elif values == ["3", "3", "3"]:
        special_matches[player] = "333"
    elif values == ["4", "4", "4"]:
        special_matches[player] = "444"
    elif values == ["5", "5", "5"]:
        special_matches[player] = "555"
    elif values == ["6", "6", "6"]:
        special_matches[player] = "666"
    elif values == ["7", "7", "7"]:
        special_matches[player] = "777"
    elif values == ["8", "8", "8"]:
        special_matches[player] = "888"
    elif values == ["9", "9", "9"]:
        special_matches[player] = "999"
    elif values == ["10", "10", "10"]:
        special_matches[player] = "101010"
    elif values == ["J", "J", "J"]:
        special_matches[player] = "JJJ"
    elif values == ["Q", "Q", "Q"]:
        special_matches[player] = "QQQ"
    elif values == ["K", "K", "K"]:
        special_matches[player] = "KKK"
    elif values == ["A", "A", "A"]:
        special_matches[player] = "AAA"
    elif "".join(values) in special_permutations:
        special_matches[player] = "JQK"
    else:
        total = sum(value_map[card[:-1]] for card in hand)
        score = total % 10
        scores[player] = score
        print(f"Score = {score}")

getMatch = {}
if special_matches:
    print(f"\nSpecial Card Winners:\n")
    for player, match in special_matches.items():
        getMatch[player] = match
        print(f"{player} wins with special card: {match}")

if getMatch:
    for winPlayer, winMatch in getMatch.items():
        if winMatch in special_cards:
            print(f"\nLast winner is {winPlayer} with card: {winMatch}")
else:
    max_score = max(scores.values())
    winners = [player for player, score in scores.items() if score == max_score]
    print(f"\nWinner(s):")
    for winner in winners:
        print(f"{winner}")

for hand in hands.values():
    for card in hand:
        if card in cards:
            cards.remove(card)

print("\nLast Card: ", len(cards))
print("\n", cards)
