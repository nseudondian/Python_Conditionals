# Generate a secret number manually between 1 and 10
number = 3

# Get user's guess
guess = int(input("Guess the secret number (between 1 and 10): "))

# Check the guess
if guess == number:
    print(f"Congratulations! You guessed the secret number. The secret number is {number}")
elif guess < number:
    print(f"Too low! {guess} is lower than {number}.")
else:
    print(f"Too high! {guess} is higher than {number}.")


