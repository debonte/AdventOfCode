def loadFile(filePath: str = "Data\\Day06.txt") -> list[int]:
    with open(filePath, "r") as reader:
        input = reader.readline()
        rawFish = [int(x) for x in input.split(",")]
        fish = [0,0,0,0,0,0,0,0,0]
        for i in range(9):
            fish[i] = len([x for x in rawFish if x == i])
        return fish

def runSimulationOnce(fish: list[int]) -> list[int]:
    addFish = fish[0]
    resultFish = [0,0,0,0,0,0,0,0,0]
    for i in range(8):
        resultFish[i] = fish[i + 1]
    resultFish[6] = resultFish[6] + addFish
    resultFish[8] = addFish
    return resultFish

def runSimulation(fish: list[int], count: int) -> list[int]:
    for _ in range(count):
        # import time
        # startTime = time.time()
        fish = runSimulationOnce(fish)
        # print(fish)
        # duration = time.time() - startTime
        # print(str(i) + ": " + str(len(fish)) + " (" + str(duration) + ")")
    return fish

fish = loadFile()
# print(fish)
fish = runSimulation(fish, 256)
print(sum(fish))