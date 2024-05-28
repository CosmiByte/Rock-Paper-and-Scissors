import random

choices = ["rock", "paper", "scissors"]
game_count = 0


def determine_win(user: str, bot: str):
    if user == bot:
        return "It's a tie."
    elif (user == "scissors" and bot == "paper") or \
            (user == "rock" and bot == "scissors") or \
            (user == "paper" and bot == "rock"):
        return f"You win! Bot selected {bot}."
    else:
        return f"You lose! Bot selected {bot}."


def get_choices():
    bot_choice = random.choice(choices)
    user_choice = input("Select your choice (rock, paper, scissors): ").lower()
    while user_choice not in choices:
        print("Invalid choice, please try again.")
        user_choice = input("Select your choice (rock, paper, scissors): ").lower()
    return user_choice, bot_choice


def proceed(y_n):
    if y_n.lower() == "y":
        return True
    elif y_n.lower() == "n":
        return False
    else:
        return "Invalid Input"


def play():
    global game_count
    while True:
        game_count += 1
        user_choice, bot_choice = get_choices()
        print(determine_win(user_choice, bot_choice))

        dec = input("Do you want to play again? (y/n): ").lower()
        while proceed(dec) == "Invalid Input":
            print("Invalid input, please enter 'y' or 'n'.")
            dec = input("Do you want to play again? (y/n): ").lower()

        if proceed(dec):
            print("Proceeding...")
        else:
            print(f"Leaving game... | {game_count} game(s) played.")
            break


play()
