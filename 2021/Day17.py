from typing import Dict, Set, Tuple
from xmlrpc.client import MAXINT


def solve(minX: int, maxX: int, minY: int, maxY: int) -> None:
    # smallestMinSteps = MAXINT
    # biggestMaxSteps = 0

    xStartVelToSuccessSteps: Dict[int, range] = dict()
    for startvelX in range(1, maxX + 1):
        steps = 0
        velX = startvelX
        posX = 0
        while posX < minX:
            posX += velX
            velX -= 1
            steps += 1
            if velX <= 0:
                break

        if posX < minX or posX > maxX:
            continue

        minSteps = steps
        maxSteps = steps

        # if minSteps < smallestMinSteps:
        #     smallestMinSteps = minSteps

        if velX == 0:
            xStartVelToSuccessSteps[startvelX] = range(minSteps, MAXINT)
            continue

        while True:
            posX += velX
            velX -= 1

            if posX > maxX:
                break;

            maxSteps += 1
            if velX <= 0:
                break

        if velX == 0:
            xStartVelToSuccessSteps[startvelX] = range(minSteps, MAXINT)
            continue

        # if maxSteps > biggestMaxSteps:
        #     biggestMaxSteps = maxSteps

        xStartVelToSuccessSteps[startvelX] = range(minSteps, maxSteps + 1)
        # print(f"startvelX: {startvelX} works -- {minSteps}-{maxSteps} steps")

    successVels: Set[Tuple[int, int]] = set()

    for startvelY in range(minY, -minY + 1):
        steps = 0
        velY = startvelY
        posY = 0
        while posY > maxY:
            posY += velY
            velY -= 1
            steps += 1

        if posY < minY or posY > maxY:
            continue

        minSteps = steps
        maxSteps = steps

        while True:
            posY += velY
            velY -= 1

            if posY < minY:
                break

            maxSteps += 1

        # if minSteps > biggestMaxSteps or maxSteps < smallestMinSteps:
        #     continue

        # rangeY = range(minSteps, maxSteps + 1)

        for startvelX in xStartVelToSuccessSteps:
            rangeX = xStartVelToSuccessSteps[startvelX]
            if maxSteps >= rangeX.start and minSteps < rangeX.stop:
                successVels.add((startvelX, startvelY))
                print(f"{startvelX},{startvelY}")

        # print(f"startvelY: {startvelY} works --{minSteps}-{maxSteps} steps")

    print(len(successVels))


#solve(20, 30, -10, -5)
solve(175, 227, -134, -79)
