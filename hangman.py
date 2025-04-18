import random

def hangman():
    print("Welcome to Hangman!")

    # List of words to choose from
    word_list = ["python", "hangman", "programming", "developer", "computer"]
    secret_word = random.choice(word_list).lower()
    guessed_letters = []
    attempts = 6  # Number of wrong attempts allowed

    print(f"Guess the word! It has {len(secret_word)} letters.")
    print("_ " * len(secret_word))

    while attempts > 0:
        # Display the current state of the word
        display_word = ''.join([letter if letter in guessed_letters else "_" for letter in secret_word])
        print(f"\nWord: {display_word}")
        
        # Get user input
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Oops! '{guess}' is not in the word. Attempts remaining: {attempts}")

        if "_" not in display_word:
            print(f"\nCongratulations! You've guessed the word: {secret_word}")
            break

    if attempts == 0:
        print(f"\nGame Over! The word was: {secret_word}")

# Start the game
hangman()