import random


def guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    attempts = 0
    max_attempts = 10  # You can adjust the maximum number of attempts

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while attempts < max_attempts:
        try:
            # Get user input
            guess = int(input("Take a guess: "))

            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts + 1} attempts!")
                break
            elif guess < secret_number:
                print("Try a higher number.")
            else:
                print("Try a lower number.")

            attempts += 1
            remaining_attempts = max_attempts - attempts
            print(f"You have {remaining_attempts} attempts remaining.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")


if __name__ == "__main__":
    guessing_game()
