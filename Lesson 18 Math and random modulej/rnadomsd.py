import random
options={"rock","paper","scissors"}
user_choice= input("Enter rock,paper,scissors:")
computer_choice=random.choice(list(options))
if user_choice==computer_choice:
    print("A tie")
elif user_choice=="rock" and computer_choice=="scissors":
    print("You win")
elif user_choice=="paper" and computer_choice=="rock":
    print("You won")
elif user_choice == "scissors" and computer_choice=="paper":
    print("You won")
else:
    print("You lost")