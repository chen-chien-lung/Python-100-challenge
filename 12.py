# Question:
# Write a program, which will find all such numbers between 1000
# and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

ans = []
for number in range(1000, 3001):
    check = True
    for digit in str(number):
        if int(digit) % 2 != 0:
            check = False
    if check:
        ans.append(number)

print(ans)