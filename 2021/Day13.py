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

class Fold:
    value: int
    horizontal: bool

    def __init__(self, value: int, horizontal: bool):
        self.value = value
        self.horizontal = horizontal

    @staticmethod
    def parse(string: str):
        string = string[11:]
        parts = string.split("=")
        horizontal = parts[0] == "y"
        value = int(parts[1])
        return Fold(value, horizontal)

class Instructions:
    points: list[Point]
    folds: list[Fold]

    def __init__(self, points: list[Point], folds: list[Fold]):
        self.points = points
        self.folds = folds

class Map:
    map: list[list[str]]

    def __init__(self, points: list[Point]):
        width = max(points, key = lambda p: p.x).x + 1
        height = max(points, key = lambda p: p.y).y + 1
        self.map = [ ["." for _ in range(width) ] for _ in range(height) ]

        for point in points:
            self.map[point.y][point.x] = "#"

    def height(self) -> int:
        return len(self.map)

    def width(self) -> int:
        return len(self.map[0])

    def dotCount(self) -> int:
        result = 0
        for x in range(self.width()):
            for y in range(self.height()):
                if self.map[y][x] == "#":
                    result = result + 1
        return result

    def fold(self, fold: Fold):
        newMap: list[list[str]]
        if fold.horizontal:
            newHeight = int((self.height() - 1) / 2)
            newMap = [ ["." for _ in range(self.width()) ] for _ in range(newHeight) ]
            for x in range(self.width()):
                for y in range(newHeight):
                    newMap[y][x] = self.map[y][x]
                    if self.map[self.height() - y - 1][x] == "#":
                        newMap[y][x] = "#"
        else:
            newWidth = int((self.width() - 1) / 2)
            newMap = [ ["." for _ in range(newWidth) ] for _ in range(self.height()) ]
            for x in range(newWidth):
                for y in range(self.height()):
                    newMap[y][x] = self.map[y][x]
                    if self.map[y][self.width() - x - 1] == "#":
                        newMap[y][x] = "#" 
        self.map = newMap
            
    def print(self):
        for y in range(self.height()):
            print(*self.map[y], sep = "")


def loadFile(filePath: str = "Data\\Day13.txt") -> Instructions:
    with open(filePath, "r") as reader:
        lines = [line.strip() for line in reader.readlines()]
        lines = [line for line in lines if len(line) > 0]
        points = [Point.parse(line.strip()) for line in lines if not line.startswith("fold")]
        folds = [Fold.parse(line.strip()) for line in lines if line.startswith("fold")]
        return Instructions(points, folds)

instructions = loadFile()
map = Map(instructions.points)
for fold in instructions.folds:
    map.fold(fold)
map.print()
print(map.dotCount())