class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @staticmethod
    def parse(string: str):
        values = string.split(",")
        x = int(values[0])
        y = int(values[1])
        return Point(x, y)

MAP_SIZE = 1000
map = [ [0 for _ in range(MAP_SIZE) ] for _ in range(MAP_SIZE) ]

class Line:
    start: Point
    end: Point

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

        shouldReverse = False
        if self.isHorizontal():
            shouldReverse = self.start.x > self.end.x
        elif self.isVertical():
            shouldReverse = self.start.y > self.end.y
        else:
            shouldReverse = self.start.x > self.end.x

        if shouldReverse:
            self.start = end
            self.end = start
    
    def isHorizontal(self) -> bool:
        return self.start.y == self.end.y

    def isVertical(self) -> bool:
        return self.start.x == self.end.x

    def isHorizontalOrVertical(self) -> bool:
        return self.isHorizontal() or self.isVertical()

    def applyToMap(self):
        if self.isVertical():
            for y in range(self.start.y, self.end.y + 1):
                map[y][self.start.x] = map[y][self.start.x] + 1
        elif self.isHorizontal():
            for x in range(self.start.x, self.end.x + 1):
                map[self.start.y][x] = map[self.start.y][x] + 1
        else:
            yIncrement = 1
            if self.start.y > self.end.y:
                yIncrement = -1
            length = self.end.x - self.start.x + 1
            for i in range(length):
                map[self.start.y + (i * yIncrement)][self.start.x + i] = map[self.start.y + (i * yIncrement)][self.start.x + i] + 1     

    @staticmethod
    def parse(string: str):
        values = string.split(" -> ")
        start = Point.parse(values[0])
        end = Point.parse(values[1])
        return Line(start, end)

def loadFile(filePath: str = "Data\\Day05.txt") -> list[Line]:
    with open(filePath, "r") as reader:
        return [Line.parse(line) for line in reader.readlines()]

def createCountMap(filterOutDiagonals: bool):
    lines = loadFile()
    if filterOutDiagonals:
        lines = [line for line in lines if line.isHorizontalOrVertical()]
    for line in lines:
        line.applyToMap()

    # for line in map:
    #     print(line)

    result = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] > 1:
                result = result + 1

    print(result)

# createCountMap(True)
createCountMap(False)