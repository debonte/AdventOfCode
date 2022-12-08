from __future__ import annotations
from dataclasses import dataclass


class TerminalOutput:
    pass

@dataclass
class ChangeDirectoryCommand(TerminalOutput):
    targetDir: str

class ListCommand(TerminalOutput):
    pass

@dataclass
class DirectoryInfo(TerminalOutput):
    name: str

@dataclass
class FileInfo(TerminalOutput):
    size: int
    name: str

def parseCommand(line: str) -> TerminalOutput:
    if line[2] == "l":
        return ListCommand()

    return ChangeDirectoryCommand(line[5:])
    
def parseEntity(line: str) -> TerminalOutput:
    if line.startswith("dir"):
        return DirectoryInfo(line[4:])

    parts = line.split(" ")
    return FileInfo(int(parts[0]), parts[1])

def parseLine(line: str) -> TerminalOutput:
    if line.startswith("$"):
        return parseCommand(line)
    else:
        return parseEntity(line)

def loadFile(filePath: str) -> list[TerminalOutput]:
    with open(filePath, "r") as reader:
        lines = [x.strip() for x in reader.readlines()]

        result: list[TerminalOutput] = []

        for line in lines:
            result.append(parseLine(line))                

        return result

class Directory:
    def __init__(self, name: str, parent: "Directory" | None):
        self.name = name
        self.files: list[FileInfo] = []
        self.dirs: dict[str, "Directory"] = {}
        self.size = 0
        self.parent = parent

    def calculateSize(self):
        for child in self.dirs:
            self.dirs[child].calculateSize()

        self.size = sum([file.size for file in self.files]) + sum([dir.size for dir in iter(self.dirs.values())])

    def part1Answer(self) -> int:
        result = 0
        for child in self.dirs:
            result += self.dirs[child].part1Answer()

        if self.size <= 100_000:
            result += self.size

        return result

    def part2Answer(self, spaceNeeded: int) -> "Directory" | None:
        bestDirectory: "Directory" | None = None
        for child in self.dirs:
            childResult = self.dirs[child].part2Answer(spaceNeeded)
            if childResult != None and (bestDirectory == None or bestDirectory.size > childResult.size):
                bestDirectory = childResult

        if self.size > spaceNeeded and (bestDirectory == None or bestDirectory.size > self.size):
            return self

        return bestDirectory


def part1(lines: list[TerminalOutput]) -> int:
    root = Directory("/", None)
    current = root

    for line in lines:
        if isinstance(line, ChangeDirectoryCommand):
            if line.targetDir == "/":
                current = root
            elif line.targetDir == ".." and current.parent:
                current = current.parent
            else:
                current = current.dirs[line.targetDir]
        elif isinstance(line, DirectoryInfo):
            newDir = Directory(line.name, current)
            current.dirs[line.name] = newDir
        elif isinstance(line, FileInfo):
            current.files.append(line)

    root.calculateSize()

    # return root.part1Answer()

    spaceFree = 70_000_000 - root.size
    spaceNeeded = 30_000_000 - spaceFree

    bestDirectory = root.part2Answer(spaceNeeded)
    if bestDirectory:
        return bestDirectory.size

    return -1


lines = loadFile("Data\\Day07.txt")
print(part1(lines))