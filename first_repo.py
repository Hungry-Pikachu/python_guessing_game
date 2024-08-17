
import random

def guess_number():
    secret_number = random.randint(0, 9)
    attempts = 3

    print("Guess the secret number between 0 and 9. You have 3 attempts.")

    for attempt in range(attempts):
        guess = input(f"Attempt {attempt + 1}: ").strip()

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)

        if guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            return
        else:
            print("Incorrect guess.")

    print(f"Sorry, you've used all your attempts. The secret number was {secret_number}.")

    while True:
        try_again = input("Do you want to try again? (yes/no): ").strip().lower()
        if try_again == 'yes':
            guess_number()
            break
        elif try_again == 'no':
            print("Thank you for playing!")
            break
        else:
            print("Please enter 'yes' or 'no'.")

# Start the game
guess_number()
