# for character in 'Programming':
#     print(character)

    # | range(start, stop[, step]) -> range
# for counter in range(2, 20, 3):
#     print(counter)
    # Use the range function and a for statement to calculate the
    # total of the integers from 0 through  1, 000, 000.
    # object

    # total = 0
    # for counter in range(100):
    #     total += counter
    #     print(total)

        # A class of ten students took a quiz.Their grades (integers in the range 0 – 100) are
        # 98, 76, 71, 87, 83, 90, 57, 79, 82, 94. Determine the class average on the quiz.
totalScore = 0
Average = 0

studentScore = [ 98, 76, 71, 87, 83, 90, 57, 79, 82, 94]
for score in studentScore:
    totalScore+= score

Average = totalScore / len(studentScore)
print(Average)
