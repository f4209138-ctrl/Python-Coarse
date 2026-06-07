test_dict = {"Codingal": 3, "is": 2, "best": 2, "for": 2, "Coding": 1}

print("The test dictionary is:", test_dict)
user_input = input("Enter the value you want to check the frequency of: ")

if user_input.isdigit() or (
    user_input.startswith("-") and user_input[1:].isdigit()
):
    search_value = int(user_input)
else:
    search_value = user_input

frequency = list(test_dict.values()).count(search_value)

print(f"The frequency of the value {search_value} is: {frequency}")