from dataclasses import dataclass

@dataclass
class Move:
    count: int
    source: int
    dest: int

def loadFile(filePath: str) -> list[Move]:
    with open(filePath, "r") as reader:
        lines = [x.strip() for x in reader.readlines()]

        # move 1 from 2 to 1
        moves: list[Move] = []
        for line in lines:
            (_, count, _, source, _, dest) = line.split(" ")
            
            moves.append(Move(int(count), int(source) - 1, int(dest) - 1))

        return moves

def run(stacks: list[list[str]], moves: list[Move]):
    for move in moves:
        # Part 1
        # for i in range(move.count):
        #     stacks[move.dest].append(stacks[move.source].pop())

        # Part 2
        startIndex = len(stacks[move.source]) - move.count
        stacks[move.dest] += stacks[move.source][startIndex : len(stacks[move.source])]
        stacks[move.source] = stacks[move.source][0 : startIndex]

moves = loadFile("Data\\Day05.txt")

# Day05Example.txt:
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
#stacks = [["Z", "N"], ["M", "C", "D"], ["P"]]

# Day05.txt
#     [C]         [Q]         [V]    
#     [D]         [D] [S]     [M] [Z]
#     [G]     [P] [W] [M]     [C] [G]
#     [F]     [Z] [C] [D] [P] [S] [W]
# [P] [L]     [C] [V] [W] [W] [H] [L]
# [G] [B] [V] [R] [L] [N] [G] [P] [F]
# [R] [T] [S] [S] [S] [T] [D] [L] [P]
# [N] [J] [M] [L] [P] [C] [H] [Z] [R]
#  1   2   3   4   5   6   7   8   9 
stacks = [
    ["N", "R", "G", "P"],
    ["J", "T", "B", "L", "F", "G", "D", "C"],
    ["M", "S", "V"],
    ["L", "S", "R", "C", "Z", "P"],
    ["P", "S", "L", "V", "C", "W", "D", "Q"],
    ["C", "T", "N", "W", "D", "M", "S"],
    ["H", "D", "G", "W", "P"],
    ["Z", "L", "P", "H", "S", "C", "M", "V"],
    ["R", "P", "F", "L", "W", "G", "Z"]
]

run(stacks, moves)

print("".join([stack.pop() for stack in stacks]))