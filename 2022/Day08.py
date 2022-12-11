def loadFile(filePath: str) -> list[list[int]]:
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

def getVisibility(grid: list[list[int]]) -> int:#list[list[bool]]:
    numLines = len(grid)
    lineWidth = len(grid[0])
    shortestView = [ [10 for _ in range(lineWidth) ] for _ in range(numLines) ]

    # Look from left
    for iLine in range(numLines):
        tallestSoFar = -1
        for iChar in range(lineWidth):
            if tallestSoFar < shortestView[iLine][iChar]:
                shortestView[iLine][iChar] = tallestSoFar

            if grid[iLine][iChar] > tallestSoFar:
                tallestSoFar = grid[iLine][iChar]            

    # Look from right
    for iLine in range(numLines):
        tallestSoFar = -1
        for iChar in reversed(range(lineWidth)):
            if tallestSoFar < shortestView[iLine][iChar]:
                shortestView[iLine][iChar] = tallestSoFar

            if grid[iLine][iChar] > tallestSoFar:
                tallestSoFar = grid[iLine][iChar]            

    # Look from top
    for iChar in range(lineWidth):
        tallestSoFar = -1
        for iLine in range(numLines):
            if tallestSoFar < shortestView[iLine][iChar]:
                shortestView[iLine][iChar] = tallestSoFar

            if grid[iLine][iChar] > tallestSoFar:
                tallestSoFar = grid[iLine][iChar]
            
    # Look from bottom
    for iChar in range(lineWidth):
        tallestSoFar = -1
        for iLine in reversed(range(numLines)):
            if tallestSoFar < shortestView[iLine][iChar]:
                shortestView[iLine][iChar] = tallestSoFar

            if grid[iLine][iChar] > tallestSoFar:
                tallestSoFar = grid[iLine][iChar]
            
    # Determine visibility
    # visibility = [ [False for _ in range(lineWidth) ] for _ in range(numLines) ]
    numVisible = 0
    for iLine in range(numLines):
        for iChar in range(lineWidth):
            if grid[iLine][iChar] > shortestView[iLine][iChar]:
                numVisible += 1
                # visibility[iLine][iChar] = True

    return numVisible

def getBestScenicScore(grid: list[list[int]]) -> int:
    numLines = len(grid)
    lineWidth = len(grid[0])
    leftScore = [ [0 for _ in range(lineWidth) ] for _ in range(numLines) ]
    rightScore = [ [0 for _ in range(lineWidth) ] for _ in range(numLines) ]
    topScore = [ [0 for _ in range(lineWidth) ] for _ in range(numLines) ]
    bottomScore = [ [0 for _ in range(lineWidth) ] for _ in range(numLines) ]

    # Look to left
    for iLine in range(numLines):
        lastTreeOfHeight: list[int] = [0 for _ in range(10)]
        for iChar in range(lineWidth):
            treeHeight = grid[iLine][iChar]
            leftScore[iLine][iChar] = iChar - max(lastTreeOfHeight[treeHeight:])
            lastTreeOfHeight[treeHeight] = iChar            

    # Look to right
    for iLine in range(numLines):
        lastTreeOfHeight: list[int] = [lineWidth - 1 for _ in range(10)]
        for iChar in reversed(range(lineWidth)):
            treeHeight = grid[iLine][iChar]
            rightScore[iLine][iChar] = min(lastTreeOfHeight[treeHeight:]) - iChar
            lastTreeOfHeight[treeHeight] = iChar            

    # Look to top
    for iChar in range(lineWidth):
        lastTreeOfHeight: list[int] = [0 for _ in range(10)]
        for iLine in range(numLines):
            treeHeight = grid[iLine][iChar]
            topScore[iLine][iChar] = iLine - max(lastTreeOfHeight[treeHeight:])
            lastTreeOfHeight[treeHeight] = iLine            
            
    # Look to bottom
    for iChar in range(lineWidth):
        lastTreeOfHeight: list[int] = [lineWidth - 1 for _ in range(10)]
        for iLine in reversed(range(numLines)):
            treeHeight = grid[iLine][iChar]
            bottomScore[iLine][iChar] = min(lastTreeOfHeight[treeHeight:]) - iLine
            lastTreeOfHeight[treeHeight] = iLine            
            
    # Scoring
    bestScore = 0
    for iLine in range(numLines):
        for iChar in range(lineWidth):
            left = leftScore[iLine][iChar]
            right = rightScore[iLine][iChar]
            top = topScore[iLine][iChar]
            bottom = bottomScore[iLine][iChar]

            score = leftScore[iLine][iChar] * rightScore[iLine][iChar] * topScore[iLine][iChar] * bottomScore[iLine][iChar]
            if score > bestScore:
                bestScore = score
            
    return bestScore


grid = loadFile("Data\\Day08.txt")
# print(getVisibility(grid))
print(getBestScenicScore(grid))
