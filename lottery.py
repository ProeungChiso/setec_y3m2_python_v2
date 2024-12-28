import random


def generate_lottery_numbers(num_count, num_range):
    """Generate a set of random lottery numbers."""
    return set(random.sample(range(1, num_range + 1), num_count))


def get_player_numbers(num_count, num_range):
    """Get player's lottery numbers."""
    print(f"Enter {num_count} unique numbers between 1 and {num_range}:")
    player_numbers = set()
    while len(player_numbers) < num_count:
        try:
            num = int(input(f"Enter number {len(player_numbers) + 1}: "))
            if num < 1 or num > num_range:
                print(f"Number must be between 1 and {num_range}.")
            elif num in player_numbers:
                print("You already entered this number. Choose a different one.")
            else:
                player_numbers.add(num)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return player_numbers

def main():
    num_count = 1  # Number of numbers to pick
    num_range = 49  # Range of numbers to pick from (1 to num_range)

    print("Welcome to the Lottery Game!")

    # Generate winning lottery numbers
    winning_numbers = generate_lottery_numbers(num_count, num_range)
    print("\nWinning numbers are:", winning_numbers)

    # Get player's numbers
    player_numbers = get_player_numbers(num_count, num_range)

    # Compare numbers and display results
    matching_numbers = player_numbers & winning_numbers
    print("\nYour numbers:", player_numbers)
    print(f"You matched {len(matching_numbers)} numbers: {matching_numbers}")

    if len(matching_numbers) == num_count:
        print("Congratulations! You hit the jackpot!")
    else:
        print("Better luck next time!")


if __name__ == "__main__":
    main()