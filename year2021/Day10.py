from collections import deque

def loadFile(filePath: str = "Data\\Day10.txt") -> list[str]:
    with open(filePath, "r") as reader:
        return [line.strip() for line in reader.readlines()]

def getExpectedClosingChar(openingChar: str) -> str:
    match openingChar:
        case "(":
            return ")"   
        case "[":
            return "]"  
        case "{":
            return "}"   
        case "<":
            return ">"
    return "X"

def getFirstIllegalCharacter(line: str) -> str:
    stack: deque[str] = deque()

    for char in line:
        match char:
            case "(" | "[" | "{" | "<":
                stack.append(char)
            case ")" | "]" | "}" | ">":
                matchingChar = stack.pop()
                expectedChar = getExpectedClosingChar(matchingChar)
                if char != expectedChar:
                    return char

    return ""
        
def getSyntaxErrorScore(lines: list[str]) -> int:
    result = 0
    for line in lines:
        illegal = getFirstIllegalCharacter(line)
        if illegal == ')':
            result += 3
        elif illegal == ']':
            result += 57
        elif illegal == '}':
            result += 1197
        elif illegal == '>':
            result += 25137
    
    return result

def getIncompleteStack(line: str) -> deque[str] | None:
    stack: deque[str] = deque()

    for char in line:
        match char:
            case "(" | "[" | "{" | "<":
                stack.append(char)
            case ")" | "]" | "}" | ">":
                matchingChar = stack.pop()
                expectedChar = getExpectedClosingChar(matchingChar)
                if char != expectedChar:
                    return None

    return stack

def getCompletionScore(lines: list[str]) -> int:
    scores: list[int] = []

    for line in lines:
        stack = getIncompleteStack(line)
        if stack == None:
            continue
        
        score = 0
        for char in reversed(stack):
            score *= 5

            if char == '(':
                score += 1
            elif char == '[':
                score += 2
            elif char == '{':
                score += 3
            elif char == '<':
                score += 4

        scores.append(score)

    scores.sort()    
    return scores[int(len(scores) / 2)]

lines = loadFile()
print(getSyntaxErrorScore(lines))
print(getCompletionScore(lines))