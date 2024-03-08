import random

def guessing_game():
    print("I am thinking of a number between 1 and 100. Can you guess the number?")

    secret_number = random.randint(1,100)
    user_attempts = 0
    user_guess = None

    while user_guess != secret_number:
        user_guess = input("Enter your number: ")
        user_guess = int(user_guess)
        user_attempts += 1
        
        if user_guess < secret_number:
            print("Too  low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number {secret_number} in {user_attempts} attempts.")
    
    play_again = input("Would you like to play again? (y/n) ")
    if play_again.lower() == 'y':
        guessing_game()
    else:
        print("Thanks for playing!")

guessing_game()

