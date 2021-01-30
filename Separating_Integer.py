# 3.9 (Separating the Digits in an Integer) In Exercise 2.11, you wrote a script that separated
# a five-digit integer into its individual digits and displayed them. Reimplement your
# script to use a loop that in each iteration “picks off” one digit (left to right) using the //
# and % operators, then displays that digit.
num = int(input("Enter 5-digit integer \n"))
for number in range(4, 0, -1):
    # divisor = number // (10**number)
    num%=(10)
    print(num)
