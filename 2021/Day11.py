from collections import deque

def loadFile(filePath: str = "Data\\Day11.txt") -> list[list[int]]:
    with open(filePath, "r") as reader:
        numLines = 0
        lineWidth = 0
        for line in reader.readlines():
            if lineWidth == 0:
                lineWidth = len(line.strip())
            numLines += 1

        map = [ [10 for _ in range(lineWidth) ] for _ in range(numLines) ]

        reader.seek(0)

        iLine = 0
        for line in reader.readlines():
            iChar = 0
            for char in line.strip():
                map[iLine][iChar] = int(char)
                iChar += 1
            iLine += 1

    return map

class Point:
    line: int
    char: int

    def __init__(self, line: int, char: int):
        self.line = line
        self.char = char

def flashPoint(point: Point, map: list[list[int]], stack: deque[Point]):
    if (point.line >= 0 and point.line < len(map) and point.char >= 0 and point.char < len(map[0])):
        map[point.line][point.char] += 1
        if map[point.line][point.char] > 9:
            stack.append(point)

def flashSquare(center: Point, map: list[list[int]], stack: deque[Point]):
    flashPoint(Point(center.line - 1, center.char - 1), map, stack)
    flashPoint(Point(center.line - 1, center.char), map, stack)
    flashPoint(Point(center.line - 1, center.char + 1), map, stack)
    flashPoint(Point(center.line, center.char - 1), map, stack)
    flashPoint(Point(center.line, center.char + 1), map, stack)
    flashPoint(Point(center.line + 1, center.char - 1), map, stack)
    flashPoint(Point(center.line + 1, center.char), map, stack)
    flashPoint(Point(center.line + 1, center.char + 1), map, stack)

def allFlashed(hasFlashed: list[list[bool]]) -> bool:
    for line in range(len(map)):
        for char in range(len(map[0])):
            if not hasFlashed[line][char]:
                return False
    return True

def runSimulationOnce(map: list[list[int]]) -> int:
    numberOfFlashes = 0
    for line in range(len(map)):
        for char in range(len(map[0])):
            map[line][char] += 1

    hasFlashed: list[list[bool]] = [ [ False for _ in range(len(map[0])) ] for _ in range(len(map)) ]
    stack: deque[Point] = deque()
    
    for line in range(len(map)):
        for char in range(len(map[0])):
            if map[line][char] > 9:
                stack.append(Point(line, char))

    while len(stack) > 0:
        point = stack.pop()
        if not hasFlashed[point.line][point.char]:
            hasFlashed[point.line][point.char] = True
            numberOfFlashes += 1
            flashSquare(point, map, stack)

    if allFlashed(hasFlashed):
        print("All flashed")

    for line in range(len(map)):
        for char in range(len(map[0])):
            if hasFlashed[line][char]:
                map[line][char] = 0

    return numberOfFlashes

def runSimulation(map: list[list[int]], iterations: int):
    totalNumberOfFlashes = 0
    for iteration in range(iterations):
        print(iteration)
        totalNumberOfFlashes += runSimulationOnce(map)
    return totalNumberOfFlashes

map = loadFile()
print(runSimulation(map, 500))