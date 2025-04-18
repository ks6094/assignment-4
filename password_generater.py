import random
import string

def generate_passwords():
    print("Welcome to the Random Password Generator!")

    try:
        # Collect user input for the number of passwords and their lengths
        num_passwords = int(input("How many passwords do you want to generate? "))
        length = int(input("What should be the length of each password? "))
    except ValueError:
        print("Please enter valid numbers for the inputs!")
        return

    if num_passwords <= 0 or length <= 0:
        print("Both the number of passwords and their lengths must be positive integers!")
        return

    # Define the characters to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    print("\nHere are your randomly generated passwords:")
    for _ in range(num_passwords):
        # Generate a random password of the specified length
        password = ''.join(random.choice(characters) for _ in range(length))
        print(password)

# Start the password generator
generate_passwords()