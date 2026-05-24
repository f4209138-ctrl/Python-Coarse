def check_lucky_number():
    LUCKY_NUMBER = 5
    attempts = 0
    while True:
     user_input = int(input("Enter a number: "))
     LUCKY_NUMBER.append(user_input)
     attempts += 1
     if user_input == LUCKY_NUMBER:
         print("Congratulations! You guessed the lucky number in", attempts, "attempts.")
         break
     elif user_input < LUCKY_NUMBER:
        print("Too low! Try again.")
     else:
        print("Too high! Try again.")
check_lucky_number()