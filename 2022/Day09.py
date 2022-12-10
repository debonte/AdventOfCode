from dataclasses import dataclass
from enum import Enum, auto

class Direction(Enum):
    Left = auto()
    Right = auto()
    Up = auto()
    Down = auto()

@dataclass
class Move:
    dir: Direction
    distance: int

def getDirection(dir: str):
    if dir == "L":
        return Direction.Left
    elif dir == "R":
        return Direction.Right
    elif dir == "U":
        return Direction.Up
    elif dir == "D":
        return Direction.Down
    
    raise Exception("Invalid direction")
        

def loadFile(filePath: str) -> list[Move]:
    with open(filePath, "r") as reader:
        lines = [x.strip() for x in reader.readlines()]

        moves: list[Move] = []
        for line in lines:
            (dir, distance) = line.split(" ")
            moves.append(Move(getDirection(dir), int(distance)))

        return moves

def areAdjacent(a: tuple[int, int], b: tuple[int, int]) -> bool:
    return abs(a[0] - b[0]) == 1 and abs(a[1] - b[1]) == 1

def part1(input: list[Move]):
    part2(input, 2)

def part2(input: list[Move], nodeCount: int):
    visited: set[tuple[int, int]] = set()

    nodes: list[tuple[int, int]] = []
    for i in range(nodeCount):
        nodes.append((0, 0))

    visited.add((0, 0))

    for move in input:
        for _ in range(move.distance):
            head = nodes[0]
            if move.dir == Direction.Left:
                head = (head[0] - 1, head[1])
            elif move.dir == Direction.Right:
                head = (head[0] + 1, head[1])
            elif move.dir == Direction.Up:
                head = (head[0], head[1] + 1)
            elif move.dir == Direction.Down:
                head = (head[0], head[1] - 1)
            nodes[0] = head

            for i in range(1, nodeCount):
                head = nodes[i - 1]
                nextNode = nodes[i]

                if head[0] == nextNode[0]:
                    if head[1] >= nextNode[1] + 2:
                        nextNode = (nextNode[0], nextNode[1] + 1)
                    elif head[1] <= nextNode[1] - 2:
                        nextNode = (nextNode[0], nextNode[1] - 1)
                elif head[1] == nextNode[1]:
                    if head[0] >= nextNode[0] + 2:
                        nextNode = (nextNode[0] + 1, nextNode[1])
                    elif head[0] <= nextNode[0] - 2:
                        nextNode = (nextNode[0] - 1, nextNode[1])
                elif not areAdjacent(head, nextNode):
                    if head[0] > nextNode[0] and head[1] > nextNode[1]:
                        nextNode = (nextNode[0] + 1, nextNode[1] + 1)
                    elif head[0] > nextNode[0] and head[1] < nextNode[1]:
                        nextNode = (nextNode[0] + 1, nextNode[1] - 1)
                    elif head[0] < nextNode[0] and head[1] > nextNode[1]:
                        nextNode = (nextNode[0] - 1, nextNode[1] + 1)
                    elif head[0] < nextNode[0] and head[1] < nextNode[1]:
                        nextNode = (nextNode[0] - 1, nextNode[1] - 1)

                nodes[i] = nextNode

            visited.add(nodes[nodeCount - 1])
    
    print(len(visited))

input = loadFile("Data\\Day09.txt")
part1(input)
part2(input, 10)