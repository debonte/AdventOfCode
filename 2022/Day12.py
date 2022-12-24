# from copy import deepcopy
from dataclasses import dataclass
from queue import PriorityQueue

def loadFile(filePath: str) -> list[list[str]]:
    with open(filePath, "r") as reader:
        numLines = 0
        lineWidth = 0
        for line in reader.readlines():
            if lineWidth == 0:
                lineWidth = len(line.strip())
            numLines += 1

        grid = [ [ "." for _ in range(lineWidth) ] for _ in range(numLines) ]

        reader.seek(0)

        iLine = 0
        for line in reader.readlines():
            iChar = 0
            for char in line.strip():
                grid[iLine][iChar] = char
                iChar += 1
            iLine += 1

        return grid


@dataclass(order=True, frozen=True)
class Point:
    line: int
    char: int


def find(searchChar: str, grid: list[list[str]]) -> Point:
    for iLine, line in enumerate(grid):
        for iChar, char in enumerate(line):
            if char == searchChar:
                return Point(iLine, iChar)
            
    raise Exception("Character not found")


def getNeighbors(grid: list[list[str]], point: Point) -> list[Point]:
    neighbors: list[Point] = []

    if point.line > 0:
        neighbors.append(Point(point.line - 1, point.char))
    
    if point.line < len(grid) - 1:
        neighbors.append(Point(point.line + 1, point.char))

    if point.char > 0:
        neighbors.append(Point(point.line, point.char - 1))

    if point.char < len(grid[0]) - 1:
        neighbors.append(Point(point.line, point.char + 1))

    return neighbors


@dataclass(order=True)
class PriorityQueueItem:
    point: Point
    distance: int


def getLetter(grid: list[list[str]], point: Point) -> str:
        letter = grid[point.line][point.char]

        if letter == "S":
            letter = "a"
        elif letter == "E":
            letter = "z"
        
        return letter


def isLegalMove(grid: list[list[str]], start: Point, end: Point) -> bool:
    startLetter = ord(getLetter(grid, start))
    endLetter = ord(getLetter(grid, end))
    return endLetter <= startLetter + 1
    

def dijkstra(grid: list[list[str]]) -> int:
    queue: PriorityQueue[PriorityQueueItem] = PriorityQueue()
    dist: dict[Point, int] = dict()

    start = find("S", grid)
    end = find("E", grid)

    queue.put(PriorityQueueItem(start, 0))

    while not queue.empty():
        current = queue.get()

        if current.point in dist and current.distance >= dist[current.point]:
            continue

        dist[current.point] = current.distance

        print(f"{current.point.line + 1}, {current.point.char + 1} = {current.distance}")

        for testPoint in getNeighbors(grid, current.point):
            if isLegalMove(grid, current.point, testPoint):
                queue.put(PriorityQueueItem(testPoint, current.distance + 1))

    return dist[end]    


grid = loadFile("Data\\Day12.txt")
bestDistance = dijkstra(grid)
print(bestDistance)