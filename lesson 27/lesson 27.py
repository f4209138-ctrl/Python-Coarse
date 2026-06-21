import random
secret_number = random.randint(1,10)
print("Guess the secret number between 1 and 10:")
while True:
    guess = int(input())
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("You guessed it!")
        break