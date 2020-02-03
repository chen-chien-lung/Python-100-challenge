# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

sentence = input().split(" ")

letters = 0
numbers = 0
for word in sentence:
    if word.isalpha():
        letters += len(word)
    elif word.isdigit():
        numbers += len(word)
    else:
        pass

print("LETTERS ", letters)
print("NUMBERS ", numbers)