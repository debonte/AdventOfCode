def loadFile(filePath: str) -> str:
    with open(filePath, "r") as reader:
        return reader.readline().strip()

def part1(input: str) -> int:
    for i in range(3, len(input)):
        if input[i] != input[i - 1] and\
            input[i] != input[i - 2] and\
            input[i] != input[i - 3] and\
            input[i - 1] != input[i - 2] and\
            input[i - 1] != input[i - 3] and\
            input[i - 2] != input[i - 3]:
            return i + 1

    return -1

def part2(input: str, windowSize: int) -> int:
    letterCounts: dict[str, int] = {}
    
    for i in range(len(input)):
        chAdd = input[i]

        if chAdd in letterCounts:
            letterCounts[chAdd] += 1
        else:
            letterCounts[chAdd] = 1

        if i - windowSize >= 0:
            chRemove = input[i - windowSize]

            letterCounts[chRemove] -= 1

            if letterCounts[chRemove] == 0:
                del letterCounts[chRemove]

        if len(letterCounts) == windowSize:
            return i + 1

    return -1

print(part2(loadFile("Data\\Day06.txt"), 14))