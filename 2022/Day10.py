from dataclasses import dataclass

@dataclass
class Move:
    count: int
    source: int
    dest: int

def loadFile(filePath: str) -> list[int]:
    with open(filePath, "r") as reader:
        lines = [x.strip() for x in reader.readlines()]

        result: list[int] = []
        for line in lines:
            if line == "noop":
                result.append(0)
            else:
                (_, value) = line.split(" ")
                result.append(0)
                result.append(int(value))

        return result

def part1(input: list[int]):
    X = 1

    result = 0
    for i in range(len(input)):
        if i % 40 == 19:
            result += (i + 1) * X

        X += input[i]

    return result

def part2(input: list[int]):
    X = 1

    crtPos = 0
    for i in range(len(input)):
        if crtPos - 1 <= X <= crtPos + 1:
            print("#", end="")
        else:
            print(".", end="")

        X += input[i]
        crtPos += 1

        if crtPos >= 40:
            crtPos = 0
            print("")

input = loadFile("Data\\Day10.txt")
print(part1(input))
part2(input)