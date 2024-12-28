import random
from colorama import Fore, Back, Style
import emojis

num = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
suits = ("\u2663", "\u2666", "\u2665", "\u2660")

special_cards = ["111", "222", "333", "444", "555", "666", "777", "888", "999", "101010", "JJJ", "QQQ", "KKK", "AAA"]
special_permutations = ["JQK", "JKQ", "QJK", "QKJ", "KJQ", "KQJ"]

cards = [n + s for n in num for s in suits]

value_map = {
    "A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
    "8": 8, "9": 9, "10": 10, "J": 0, "Q": 0, "K": 0
}

num_players = int(input(emojis.encode(f"\n👉 {Fore.GREEN}Enter number of players: ")))

random.shuffle(cards)
hands = {'Player 1': ['A♥', 'A♣', 'A♠'], 'Player 2': ['Q♥', 'K♥', 'J♠']}

# hands = {}
# for i in range(num_players):
#     hands[f"Player {i+1}"] = [cards.pop() for _ in range(3)]

scores = {}
special_matches = {}

print(f"{Style.RESET_ALL}")
for player, hand in hands.items():
    print(emojis.encode(f"{Fore.CYAN}👾 {player} has cards {hand}{Style.RESET_ALL}"))
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
        print(f"{Fore.CYAN}Score = {score}{Style.RESET_ALL}")

getMatch = {}
if special_matches:
    print(f"\n{Fore.MAGENTA}Special Card Winners:{Style.RESET_ALL}\n")
    for player, match in special_matches.items():
        getMatch[player] = match
        print(emojis.encode(f"{Fore.MAGENTA}👾 {player} wins with special card: {match}{Style.RESET_ALL}"))

if getMatch:
    for winPlayer, winMatch in getMatch.items():
        if(winMatch in special_cards):
            print(emojis.encode(f"\n{Fore.RED}💥 Last winner is {winPlayer} with card: {winMatch}{Style.RESET_ALL}"))

else:
    max_score = max(scores.values())
    winners = [player for player, score in scores.items() if score == max_score]
    print(f"\n{Fore.BLUE}Winner(s):{Style.RESET_ALL}")
    for winner in winners:
        print(f"{Fore.BLUE}{winner}{Style.RESET_ALL}")
