# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9


sentence = input().split(" ")

upperCase = 0
lowerCase = 0

for word in sentence:
    for digit in word:
        if digit.isupper():
            upperCase += 1
        elif digit.islower():
            lowerCase += 1
        else:
            pass

print("UPPER CASE :", upperCase)
print("LOWER CASE :", lowerCase)