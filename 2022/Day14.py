from enum import StrEnum, auto
from typing import Tuple, TypeAlias


class Point:
    def __init__(self, input: str):
        nums = input.split(",")
        self.x = int(nums[0])
        self.y = int(nums[1])
        

Path: TypeAlias = list[Point]
Grid: TypeAlias = list[list[str]]


class Material(StrEnum):
    Air = "."
    Rock = "#"
    Sand = "o"


def loadFile(filePath: str) -> list[Path]:
    with open(filePath, "r") as reader:
        paths: list[list[Point]] = []
        
        for line in reader.readlines():
            line = line.strip()
            pointStrs = line.split(" -> ")
            points = [Point(p) for p in pointStrs]
            paths.append(points)

        return paths


def getGridSize(paths: list[Path]) -> Tuple[int, int]:
    maxX = 0
    maxY = 0
    
    for path in paths:
        for point in path:
            maxX = max(point.x, maxX)
            maxY = max(point.y, maxY)
            
    return (maxX + 2, maxY + 1)


def createGrid(paths: list[Path]) -> Grid:
    gridSize = getGridSize(paths)
    grid = [ [ Material.Air for _ in range(gridSize[0]) ] for _ in range(gridSize[1]) ]
    
    for path in paths:
        start =	path[0]
        for point in path[1:]:
            if point.x == start.x:
                for y in range(min(start.y, point.y), max(start.y, point.y) + 1):
                    grid[y][point.x] = Material.Rock
            else:
                for x in range(min(start.x, point.x), max(start.x, point.x) + 1):
                    grid[point.y][x] = Material.Rock
                
            start = point

    return grid


def printGrid(grid: Grid):
    for line in grid:
        print(*line, sep = "")


def tryPourSand(grid: Grid) -> bool:
    x = 500
    y = 0
    
    while y < len(grid) - 1:
        if grid[y+1][x] == Material.Air:
            y += 1
            continue
        elif grid[y+1][x-1] == Material.Air:
            y += 1
            x -= 1
            continue
        elif grid[y+1][x+1] == Material.Air:
            y += 1
            x += 1
            continue
        
        grid[y][x] = Material.Sand
        return True

    return False


paths = loadFile("Data\\Day14.txt")
grid = createGrid(paths)
# printGrid(grid)

numSandUnits = 0
while tryPourSand(grid):
    numSandUnits += 1
    # printGrid(grid)

print(numSandUnits)