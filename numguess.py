#numberguessinggamenavanith
import random

name=input("enter your name ")
print(f"hey there {name}")
def number_guessing_game():
    secret_number = random.randint(1, 20)
    attempts = 0

    print("     NUMBER GUESSING GAME")
    print("xoxoxoxoxoxoxoxoxoxoxoxoxoxoxo")
    print("Guess a number between 1 and 20!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if guess < 1 or guess > 20:
            print("Choose a number between 1 and 20.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")

        elif guess > secret_number:
            print("Too high! Try again.")

        else:
            print("\nCongratulations! You guessed it!")
            print(f"The number was {secret_number}.")
            print(f"Attempts: {attempts}")

            if attempts == 1:
                rank = "BULLSEYE!!! You are the Guessing God!"
            elif attempts <= 3:
                rank = "Legendary Guesser!"
            elif attempts <= 6:
                rank = "Great Guesser!"
            elif attempts <= 8:
                rank = "Mid Guesser!"
            else:
                rank = "Failure"

            print(f"\nYour rank: {rank}")

            return rank


def main():
    rounds = 0

    while True:
        rank = number_guessing_game()
        rounds += 1

        print("SCOREBOARD:- ")
        print(f"Rounds played: {rounds}")
        print(f"Latest rank: {rank}")
        print("================================")

        play_again = input("\nPlay again? (yes/no): ").lower()

        if play_again != "yes":
            print("\n========== FINAL SCORE ==========")
            print(f"Total rounds played: {rounds}")
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
 
