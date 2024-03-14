# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52
def getScore(ch: str) -> int:
    if ch >= "a" and ch <= "z":
        return ord(ch) - ord("a") + 1
    else:
        return ord(ch) - ord("A") + 27

def getPart1Score(lines) -> int:
    result = 0
    for line in lines:
        packSize = int(len(line) / 2)
        pack1 = line[0:packSize]
        pack2 = line[packSize:]

        for ch in pack1:
            if ch in pack2:
                result += getScore(ch)
                break

    return result

def getPart2Score(lines) -> int:
    result = 0

    elfIndex = 0
    while elfIndex < len (lines):
        elf1 = lines[elfIndex]
        elf2 = lines[elfIndex + 1]
        elf3 = lines[elfIndex + 2]

        for ch in elf1:
            if ch in elf2 and ch in elf3:
                result += getScore(ch)
                break

        elfIndex += 3

    return result

def loadFile(filePath: str) -> int:
    with open(filePath, "r") as reader:
        lines = [x.strip() for x in reader.readlines()]

        return getPart2Score(lines)

print(loadFile("Data\\Day03.txt"))