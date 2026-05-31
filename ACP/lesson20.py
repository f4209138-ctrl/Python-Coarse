start=int(input("Enter a number as the start of the range:"))
end=int(input("Enter a number as the end of the range:"))
squares=[x**2 for x in range(start,end+1)]
odd_squares=[val for val in squares if val%2!=0]
even_squares=[val for val in squares if val%2==0]
print(squares,odd_squares,even_squares)