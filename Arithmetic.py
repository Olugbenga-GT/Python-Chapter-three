# 3.8 (Arithmetic, Smallest and Largest) In Exercise 2.10, you wrote a script that input
# three integers, then displayed the sum, average, product, smallest and largest of those values.
# Reimplement your script with a loop that inputs four integers.

temp = 0
sum = 0
count = 0
largest = 0
smallest = 0
product = 1
average = 0
for number in range(5):
    num = int(input("input value \n"))
    temp = num
    count+= 1
    sum += temp
    product*=temp
    average = sum / count

    if temp > largest:
        largest = temp
    if smallest < temp:
         temp = smallest

print(f'You have {count} input \nThe sum of your inputs is {sum}\nThe product of your input is{product} \n '
      f'The average of your input is {average}\n largest input is {largest} \n smallest input is {smallest}')
