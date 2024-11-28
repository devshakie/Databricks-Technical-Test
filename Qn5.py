# Write a program that accepts a string as input, capitalizes the first letter of each
# word in the string, and then returns the result string.
# Examples:
# "hi"=> returns "Hi"
# "i love programming"=> returns "I Love Programming"

def capitalize_first_letter(word):
    return " ".join(word.capitalize() for word in word.split())

print(capitalize_first_letter("hi"))
print(capitalize_first_letter("i love programming"))
    