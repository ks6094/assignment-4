import time

def countdown_timer():
    print("Welcome to the Countdown Timer!")
    
    # Get user input for countdown time in seconds
    try:
        seconds = int(input("Enter the countdown time in seconds: "))
    except ValueError:
        print("Please enter a valid number!")
        return

    print("Countdown starts now!")
    
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds")
        time.sleep(1)  # Wait for 1 second
        seconds -= 1

    print("Countdown complete! Time's up!")

# Start the countdown timer
countdown_timer()