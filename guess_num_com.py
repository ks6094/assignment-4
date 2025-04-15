import random

# Welcome message
print("Welcome to the Guess the Number Game!")
print("Pick a number between 1 and 100.")

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

# Initialize variables
guesses = 0
correct_guess = False

# Game loop
while not correct_guess:
    try:
        user_guess = int(input("Enter your guess: "))
        guesses += 1
        
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            correct_guess = True
            print(f"Congratulations! You guessed the correct number in {guesses} attempts.")
    except ValueError:
        print("Please enter a valid number.")

# End of game
print("Thanks for playing!")