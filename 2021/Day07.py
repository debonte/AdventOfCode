from xmlrpc.client import MAXINT


def loadFile(filePath: str = "Data\\Day07.txt") -> list[int]:
    with open(filePath, "r") as reader:
        input = reader.readline()
        crabs = [int(x) for x in input.split(",")]
        crabs.sort()
        return crabs

def getFuelCost(start: int, end: int):
    distance = abs(start - end)
    return int(distance * (distance + 1) / 2)

def calculateOptimalPosition(crabs: list[int]):
    minPos = min(crabs)
    maxPos = max(crabs)

    crabCount = [ 0 for _ in range(maxPos + 1) ]
    for i in range(minPos, maxPos + 1):
        crabCount[i] = len([x for x in crabs if x == i])

    bestPos = 0
    bestFuel = MAXINT

    for i in range(minPos, maxPos + 1):
        fuel = 0
        for less in range(minPos, i):
            fuel = fuel + (crabCount[less] * getFuelCost(i, less))
        for more in range(i, maxPos + 1):
            fuel = fuel + (crabCount[more] * getFuelCost(more, i))
        if fuel < bestFuel:
            bestFuel = fuel
            bestPos = i

    print(bestPos)
    print(bestFuel)

crabs = loadFile()
calculateOptimalPosition(crabs)