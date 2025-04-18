import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'exit' to quit.\n")
    
    # List of possible choices
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        # Get user input
        user_choice = input("Your choice: ").lower()
        
        # Handle exit condition
        if user_choice == 'exit':
            print("Thanks for playing! Goodbye!")
            break
        
        # Validate user input
        if user_choice not in choices:
            print("Invalid choice! Please select 'rock', 'paper', or 'scissors'.\n")
            continue
        
        # Computer's random choice
        computer_choice = random.choice(choices)
        print(f"Computer choose: {computer_choice}")
        
        # Determine the outcome
        if user_choice == computer_choice:
            print("It's a tie!\n")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!\n")
        else:
            print("You lose!\n")

# Start the game
rock_paper_scissors()