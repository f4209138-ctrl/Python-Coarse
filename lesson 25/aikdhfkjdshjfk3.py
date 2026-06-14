import array as arr
numbers=arr.array("i",[1,3,5,3,7,9,3])
occurrences= numbers.count(3)
print(f"The number 3 occurs {occurrences} ")
numbers.reverse()
print(f"Reversed array:{numbers.tolist()}")