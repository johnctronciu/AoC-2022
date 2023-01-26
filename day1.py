# Problem 1 of 2022 Advent of Code
# Day 1: Calorie Counting ---

def CalorieCounter():
    max_cals = [0, 0, 0]
    curr_cal = 0
    with open("input.txt") as f:
        for line in f:
            if line != '\n':
                curr_cal += int(line)

            if line == '\n':
                arr_min = max_cals[0]
                for i in range(1, len(max_cals)):
                    arr_min = min(arr_min, max_cals[i])

                if curr_cal > arr_min:
                    max_cals[max_cals.index(arr_min)] = curr_cal

                curr_cal = 0

    print(max_cals)
    top_three = 0

    for i in max_cals:
        top_three += i
    print("Top three =", top_three)


if __name__ == '__main__':
    CalorieCounter()
