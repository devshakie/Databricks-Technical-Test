# Write a Python function to check whether a string is pangram or not. (Assume
# the string passed in does not have any punctuation)
# Note: Pangrams are words or sentences containing every letter of the
# alphabet at least once. For example: "The quick brown fox jumps over the
# lazy dog"

import string;
def is_pangram(word):
    alphabet = set(string.ascii_lowercase)
    return alphabet <= set(word.lower())
print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("hello"))


    