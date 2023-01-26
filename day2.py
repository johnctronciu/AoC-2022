# 2022 Advent of Code
# --- Day 2: Rock Paper Scissors ---

# X = 1 pts
# Y = 2 pts
# Z = 3 pts

# Loss = 0 pts
# Draw = 3 pts
# Win = 6 pts
def strategyGuide():
    opponent = {
        'A': "rock",
        'B': "paper",
        'C': "scissors"
    }
    user = {
        'X': "rock",
        'Y': "paper",
        'Z': "scissors"
    }
    total = 0
    with open("input") as f:
        for line in f:
            x = line.split()

            # Draw cases
            if opponent.get(x[0]) == user.get(x[1]):
                if x[1] == 'X':
                    score = 3 + 1
                elif x[1] == 'Y':
                    score = 3 + 2
                elif x[1] == 'Z':
                    score = 3 + 3

            elif x[1] == 'X':
                if x[0] == 'B':
                    score = 0 + 1
                else:
                    score = 6 + 1
            elif x[1] == "Y":
                if x[0] == 'C':
                    score = 0 + 2
                else:
                    score = 6 + 2
            elif x[1] == "Z":
                if x[0] == 'A':
                    score = 0 + 3
                else:
                    score = 6 + 3

            total += score
            print(score)
            print(total)
    print(total)


def strategyGuide2():
    total = 0
    with open("input") as f:
        for line in f:
            x = line.split()
            if x[1] == 'X':  # Must Lose
                if x[0] == 'A':  # Use Scissors
                    score = 0 + 3
                elif x[0] == 'B':  # Use rock
                    score = 0 + 1
                elif x[0] == 'C':  # Use Paper
                    score = 0 + 2
            if x[1] == 'Y':  # Must Tie
                if x[0] == 'A':  # Use Rock
                    score = 3 + 1
                elif x[0] == 'B':  # Use Paper
                    score = 3 + 2
                elif x[0] == 'C':  # Use Scissors
                    score = 3 + 3
            if x[1] == 'Z':  # Must Win
                if x[0] == 'A':  # Use Paper
                    score = 6 + 2
                elif x[0] == 'B':  # Use Scissors
                    score = 6 + 3
                elif x[0] == 'C':  # Use Rock
                    score = 6 + 1

            total += score
    print(total)


if __name__ == '__main__':
    strategyGuide()
    print("day 2")
    strategyGuide2()
