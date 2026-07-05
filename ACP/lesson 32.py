class StringReverse:
    def reverse_words(self,text):
        words = text.split()
        return " ".join(reversed(words))
reverse = StringReverse()
input_string= "Hello world from me"
output_string= reverse.reverse_words(input_string)
print(output_string)