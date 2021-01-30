# 3.2 (What’s Wrong with This Code?) What is wrong with the following code?
a = b = 7
print('a =', a, '\nb =', b)
# First, answer the question, then check your work in an IPython session


# 3.3 (What Does This Code Do?) What does the following program print?
for row in range(10):
    for column in range(10):
        print('<' if row % 2 == 1 else '>', end='')
    print()