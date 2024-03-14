from utils import getLinesFromFile


NUMBER_WORDS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def replaceNumberWords(line: str) -> str:
    i = 0
    while i < len(line):
        for numberWord in NUMBER_WORDS.items():
            if line[i:].startswith(numberWord[0]):
                line = line[:i] + numberWord[1] + line[i + len(numberWord[1]):]

        i += 1

    return line


def getNumber(line: str) -> int:
    line = replaceNumberWords(line)
    
    firstDigitIndex = 0
    while firstDigitIndex < len(line) and not line[firstDigitIndex].isdigit():
        firstDigitIndex += 1

    lastDigitIndex = len(line) - 1
    while lastDigitIndex >= 0 and not line[lastDigitIndex].isdigit():
        lastDigitIndex -= 1

    result = int(line[firstDigitIndex] + line[lastDigitIndex])
    print(f"{line} -> {result}")
    return result


lines = getLinesFromFile("Data/Day01.txt")
numbers = [getNumber(x) for x in lines]
print(sum(numbers))