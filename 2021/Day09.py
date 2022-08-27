from collections import deque

def loadFile(filePath: str = "Data\\Day09.txt") -> list[list[int]]:
    with open(filePath, "r") as reader:
        numLines = 0
        lineWidth = 0
        for line in reader.readlines():
            if lineWidth == 0:
                lineWidth = len(line.strip())
            numLines += 1

        map = [ [10 for _ in range(lineWidth + 2) ] for _ in range(numLines + 2) ]

        reader.seek(0)

        iLine = 0
        for line in reader.readlines():
            iLine += 1
            iChar = 0
            for char in line.strip():
                iChar += 1
                map[iLine][iChar] = int(char)

    return map

class Point:
    line: int
    char: int

    def __init__(self, line: int, char: int):
        self.line = line
        self.char = char

class Basin:
    start: Point
    size: int

    def __init__(self, start: Point, size: int):
        self.start = start
        self.size = size
    
def getLowPoints(map: list[list[int]]) -> list[Point]:
    result: list[Point] = []

    for line in range(len(map)):
        for char in range(len(map[0])):
            value = map[line][char]
            if (value < map[line - 1][char] and value < map[line][char - 1] and value < map[line][char + 1] and value < map[line + 1][char]):
                result.append(Point(line, char))

    return result

def getLowPointRiskSum(map: list[list[int]]) -> int:
    result = 0
    for point in getLowPoints(map):
        result += map[point.line][point.char] + 1
    return result

def exploreBasin(start: Point, map: list[list[int]], visited: list[list[bool]]) -> int:
    size = 0

    pointsToExplore: deque[Point] = deque()
    pointsToExplore.append(start)
    
    while len(pointsToExplore) > 0:
        point = pointsToExplore.pop()

        if visited[point.line][point.char] == False:
            visited[point.line][point.char] = True
            size += 1
    
        if (point.line - 1 >= 0 and map[point.line - 1][point.char] < 9 and visited[point.line - 1][point.char] == False):
            pointsToExplore.append(Point(point.line - 1, point.char))
        if (point.line + 1 < len(map) and map[point.line + 1][point.char] < 9 and visited[point.line + 1][point.char] == False):
            pointsToExplore.append(Point(point.line + 1, point.char))
        if (point.char - 1 >= 0 and map[point.line][point.char - 1] < 9 and visited[point.line][point.char - 1] == False):
            pointsToExplore.append(Point(point.line, point.char - 1))
        if (point.char + 1 < len(map[0]) and map[point.line][point.char + 1] < 9 and visited[point.line][point.char + 1] == False):
            pointsToExplore.append(Point(point.line, point.char + 1))    
    
    return size

def getBasins(map: list[list[int]]) -> list[Basin]:
    result: list[Basin] = []

    visited = [ [ False for _ in range(len(map[0])) ] for _ in range(len(map)) ]

    for point in getLowPoints(map):
        if visited[point.line][point.char]:
            continue
        
        size = exploreBasin(point, map, visited)
        result.append(Basin(point, size))
        
    return sorted(result, key=lambda basin: basin.size, reverse=True)

def getBasinProduct(map: list[list[int]]) -> int:
    result: int = 0
    for basin in getBasins(map)[0:3]:
        if result == 0:
            result = basin.size
        else:
            result *= basin.size
    return result  
    
map = loadFile()
print(getLowPointRiskSum(map))
print(getBasinProduct(map))
