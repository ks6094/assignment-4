import random

def computer_guess():
    print("Think of a number between 1 and 100, and I will try to guess it!")
    input("Press Enter when you're ready...")
    
    # Get the number of attempts
    attempts = int(input("How many attempts should I get (e.g., 5 or 10)? "))
    low = 1
    high = 100
    guessed_correctly = False
    
    while not guessed_correctly and attempts > 0:
        # Computer makes a guess
        guess = random.randint(low, high)
        print(f"My guess is: {guess}")
        
        # Get user feedback
        feedback = input("Is my guess too high (H), too low (L), or correct (C)? ").lower()
        
        if feedback == 'h':
            high = guess - 1  # Adjust the upper limit
        elif feedback == 'l':
            low = guess + 1  # Adjust the lower limit
        elif feedback == 'c':
            guessed_correctly = True
            print(f"Yay! I guessed your number, {guess}!")
            break
        else:
            print("Invalid input. Please enter H, L, or C.")
        
        # Decrease the number of attempts left
        attempts -= 1
    
    if not guessed_correctly:
        print("Oh no, I'm out of attempts! Better luck next time!")
    else:
        print("Thanks for playing!")

# Start the game
computer_guess()