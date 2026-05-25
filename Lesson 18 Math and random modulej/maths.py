import random
playing = True
number = str(random.randint(1, 9))
print("Welcome to the number guessing game!")
while playing:
    guess = input("Enter a number between 1 and 9: ")
    if guess == number:
        print("You guessed the number")
        break
    else:
        print("Wrong guess, try again.")