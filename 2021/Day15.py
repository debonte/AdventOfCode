from collections import deque
from queue import PriorityQueue
from typing import Tuple
from typing_extensions import Self


def loadFile(filePath: str = "Data\\Day15.txt") -> list[list[int]]:
    with open(filePath, "r") as reader:
        lineWidth = 0
        map: list[list[int]]

        iLine = 0
        for line in reader.readlines():
            if lineWidth == 0:
                lineWidth = len(line.strip())
                map = [ [9 for _ in range(lineWidth) ] for _ in range(lineWidth) ]

            iChar = 0
            for char in line.strip():
                map[iLine][iChar] = int(char)
                iChar += 1

            iLine += 1

    return map

def getCostDynamicProgramming(map: list[list[int]]) -> int:
    costs = [ [9999999 for _ in range(len(map)) ] for _ in range(len(map)) ]
    costs[0][0] = 0

    for i in range(1, len(map)):
        costs[0][i] = costs[0][i-1] + map[0][i]
        costs[i][0] = costs[i-1][0] + map[i][0]

    for y in range(1, len(map)):
        for x in range(1, len(map)):
            costs[y][x] = min(costs[y-1][x], costs[y][x-1]) + map[y][x]

    print()
    for y in range(len(costs)):
        print(costs[y])

    return costs[len(map) - 1][len(map) - 1]

class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other: "Point"):
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return self.x + (self.y << 16)

def getNeighbors(center: Point, mapDimension: int) -> list[Point]:
    result: list[Point] = []

    if center.x > 0:
        result.append(Point(center.x - 1, center.y))
    if center.y > 0:
        result.append(Point(center.x, center.y - 1))
    if center.x < mapDimension - 1:
        result.append(Point(center.x + 1, center.y))
    if center.y < mapDimension - 1:
        result.append(Point(center.x, center.y + 1))

    return result

class ToDoElement:
    cost: int
    point: Point

    def __init__(self, cost: int, point: Point):
        self.cost = cost
        self.point = point

    def __lt__(self, other: "ToDoElement"):
        return self.cost < other.cost

# Based on https://gist.github.com/qpwo/cda55deee291de31b50d408c1a7c8515   
def getCostDijkstrasAlgorithm(map: list[list[int]]) -> int:
    start = Point(0, 0)
    goal = Point(len(map) -1, len(map) - 1)
    infinity = 9999999
    map[0][0] = infinity # we should never look at this value, so make it extreme so if it's used we'll know

    visited = set()
    cost = { start: 0 }
    parent = { start: None }
    todo: PriorityQueue[ToDoElement] = PriorityQueue()

    todo.put(ToDoElement(0, start))

    cycles = 0
    while todo:
        cycles += 1
        if cycles % 5000 == 0:
            print(f"Cycles: {cycles}")

        while not todo.empty():
            toDoElement = todo.get() # finds lowest cost vertex
            # loop until we get a fresh vertex
            if toDoElement.point not in visited:
                break
        else: # if todo ran out
            break # quit main loop
        
        visited.add(toDoElement.point)

        if toDoElement.point == goal:
            break
        
        for neighbor in getNeighbors(toDoElement.point, len(map)):
            if neighbor in visited: # skip these to save time
                continue
            oldCost = cost.get(neighbor, infinity) # default to infinity
            newCost = cost[toDoElement.point] + map[neighbor.y][neighbor.x]
            if newCost < oldCost:
                todo.put(ToDoElement(newCost, neighbor))
                cost[neighbor] = newCost
                parent[neighbor] = toDoElement.point

    return cost[goal]

def printMap(map: list[list[int]]):
    for y in range(len(map)):
        print(*map[y], sep = "")

def createPart2Map(map: list[list[int]]):
    mapDimension = len(map)
    newMapDimension = mapDimension * 5
    newMap = [ [9999999 for _ in range(newMapDimension) ] for _ in range(newMapDimension) ]
    
    for y in range(mapDimension):
        for x in range(mapDimension):
            mapValue = map[y][x]
            for yMap in range(5):
                for xMap in range(5):
                    newMapValue = (mapValue + yMap + xMap)
                    if (newMapValue > 9):
                        newMapValue -= 9
                    newMap[y + (yMap * mapDimension)][x + (xMap * mapDimension)] = newMapValue

    return newMap

map = loadFile()
map = createPart2Map(map)
# printMap(map)
# print(getCostDynamicProgramming(map))
print(getCostDijkstrasAlgorithm(map))