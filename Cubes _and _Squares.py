# 3.7 (Table of Squares and Cubes) In Exercise 2.8, you wrote a script to calculate the
# squares and cubes of the numbers from 0 through 5, then printed the resulting values in
# table format. Reimplement your script using a for loop and the f-string capabilities you
# learned in this chapter to produce the following table with the numbers right aligned in
# each column.
# Exercises 113
# number square cube
# 0 0 0
# 1 1 1
# 2 4 8
# 3 9 27
# 4 16 64
# 5 25 125

print(f'number', f'square',  f'cube' )
for number in range(1, 6):
    print(f'{number:>4}', f'{number**2:>6}', f'{number**3:>6}')
