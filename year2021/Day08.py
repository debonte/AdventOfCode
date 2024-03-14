from operator import contains


class Entry:
    allTenPatterns: list[str]
    fourDigitOutputValue: list[str]

    def __init__(self, allTenUniqueSignalPatterns: list[str], fourDigitOutputValue: list[str]):
        self.allTenPatterns = allTenUniqueSignalPatterns
        self.fourDigitOutputValue = fourDigitOutputValue

    @staticmethod
    def parse(string: str):
        twoSides = string.split("|")
        allTenUniqueSignalPatterns = twoSides[0].split()
        fourDigitOutputValue = twoSides[1].split()
        return Entry(allTenUniqueSignalPatterns, fourDigitOutputValue)

def loadFile(filePath: str = "Data\\Day08.txt") -> list[Entry]:
    with open(filePath, "r") as reader:
        return [Entry.parse(line.strip()) for line in reader.readlines()]

def countUniqueSegmentDigitsInOutputValues(entries: list[Entry]):
    result = 0
    for entry in entries:
        for digit in entry.fourDigitOutputValue:
            digitLen = len(digit)
            if digitLen == 2 or digitLen == 3 or digitLen == 4 or digitLen == 7:
                result = result + 1
    print(result)

def patternContainsAllSegments(pattern: str, testSegments: str) -> bool:
    for char in testSegments:
        if not contains(pattern, char):
            return False

    return True

def segmentsInAllPatterns(patterns: list[str]) -> str:
    result = patterns[0]
    for char in patterns[0]:
        for otherPattern in patterns[1:]:
            if not contains(otherPattern, char):
                result = result.replace(char, "")
    return result

def segmentsContainedInPattern(pattern: str, testSegments: str) -> str:
    result = ""
    for char in testSegments:
        if contains(pattern, char):
            result = result + char

    return result

def sortPattern(pattern: str) -> str:
    chars = [char for char in pattern]
    chars.sort()
    return "".join(chars)

def deduceOutputValues(entries: list[Entry]):
    result = 0
    for entry in entries:
        # patterns with unique lengths
        one = [pattern for pattern in entry.allTenPatterns if len(pattern) == 2][0]
        seven = [pattern for pattern in entry.allTenPatterns if len(pattern) == 3][0]
        four = [pattern for pattern in entry.allTenPatterns if len(pattern) == 4][0]
        eight = [pattern for pattern in entry.allTenPatterns if len(pattern) == 7][0]

        # length 6 patterns
        nine = [pattern for pattern in entry.allTenPatterns if len(pattern) == 6 and patternContainsAllSegments(pattern, four)][0]
        zero = [pattern for pattern in entry.allTenPatterns if len(pattern) == 6 and patternContainsAllSegments(pattern, one) and not patternContainsAllSegments(pattern, nine)][0]
        six = [pattern for pattern in entry.allTenPatterns if len(pattern) == 6 and not patternContainsAllSegments(pattern, zero) and not patternContainsAllSegments(pattern, nine)][0]

        # length 5 patterns
        three = [pattern for pattern in entry.allTenPatterns if len(pattern) == 5 and patternContainsAllSegments(pattern, one)][0]
        bottomRightSegment = segmentsInAllPatterns([one, six])[0]
        five = [pattern for pattern in entry.allTenPatterns if len(pattern) == 5 and patternContainsAllSegments(pattern, bottomRightSegment) and not patternContainsAllSegments(pattern, three)][0]
        two = [pattern for pattern in entry.allTenPatterns if len(pattern) == 5 and not patternContainsAllSegments(pattern, three) and not patternContainsAllSegments(pattern, five)][0]

        # patternMap = { one: 1, two: 2, three: 3, four: 4, five: 5, six: 6, seven: 7, eight: 8, nine: 9, zero: 0 }
        patternMap = { sortPattern(one): 1, sortPattern(two): 2, sortPattern(three): 3, sortPattern(four): 4, sortPattern(five): 5, sortPattern(six): 6, sortPattern(seven): 7, sortPattern(eight): 8, sortPattern(nine): 9, sortPattern(zero): 0 }
        outputValue = 0
        reversedDigits = entry.fourDigitOutputValue
        # reversedDigits.reverse()
        for pattern in reversedDigits:
            outputValue = outputValue * 10
            outputValue = outputValue + patternMap[sortPattern(pattern)]
        
        result = result + outputValue
    print(result)

entries = loadFile()
countUniqueSegmentDigitsInOutputValues(entries)
deduceOutputValues(entries)