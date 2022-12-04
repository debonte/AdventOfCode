# (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round 
# (0 if you lost, 3 if the round was a draw, and 6 if you won).

# A Rock
# B Paper
# C Scissors

# X Rock
# Y Paper
# Z Scissors

# In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
# In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
# The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.

ROCK = 1
PAPER = 2
SCISSORS = 3

LOSE = 0
DRAW = 3
WIN = 6

def getPart1Score(round: str) -> int:
    if round == "A X":
        return DRAW + ROCK
    if round == "A Y":
        return WIN + PAPER
    if round == "A Z":
        return LOSE + SCISSORS
    if round == "B X":
        return LOSE + ROCK
    if round == "B Y":
        return DRAW + PAPER
    if round == "B Z":
        return WIN + SCISSORS
    if round == "C X":
        return WIN + ROCK
    if round == "C Y":
        return LOSE + PAPER
    if round == "C Z":
        return DRAW + SCISSORS

    raise LookupError    

# X means you need to lose
# Y means you need to end the round in a draw
# Z means you need to win.
def getPart2Score(round: str) -> int:
    if round == "A X":
        return LOSE + SCISSORS
    if round == "A Y":
        return DRAW + ROCK
    if round == "A Z":
        return WIN + PAPER
    if round == "B X":
        return LOSE + ROCK
    if round == "B Y":
        return DRAW + PAPER
    if round == "B Z":
        return WIN + SCISSORS
    if round == "C X":
        return LOSE + PAPER
    if round == "C Y":
        return DRAW + SCISSORS
    if round == "C Z":
        return WIN + ROCK

    raise LookupError    

def loadFile(filePath: str) -> int:
    with open(filePath, "r") as reader:
        lines = [x.strip() for x in reader.readlines()]

        total = 0
        for line in lines:
            score = getPart2Score(line)
            total += score

        return total

print(loadFile("Data\\Day02.txt"))