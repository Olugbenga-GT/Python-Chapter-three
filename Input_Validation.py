# 3.1 (Validating User Input) Modify the script of Fig. 3.3 to validate its inputs. For any
# input, if the value entered is other than 1 or 2, keep looping until the user enters a correct
# value. Use one counter to keep track of the number of passes, then calculate the number
# of failures after all the user’s inputs have been received.
total = 0
counter = 0
value = int(input("Please, input a number. Enter 0 to end  "))
while value != 0:
 total+= value
 counter+= 1
 value = int(input("Please, input a number.Enter 0 to end    "))
#
if counter != 0:
    print("Proces done")
    print(f'You looped {counter} times and yourn total value is {total}')
