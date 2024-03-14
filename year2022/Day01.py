def loadFile(filePath: str) -> int:
    with open(filePath, "r") as reader:
        lines = [x.strip() for x in reader.readlines()]

        elves: list[int] = []
        calories = 0
        for line in lines:
            if len(line) == 0:
                elves.append(calories)
                calories = 0
                continue

            calories += int(line)

        return elves

elves = sorted(loadFile("Data\\Day01.txt"), reverse=True)

print(sum(elves[0:3]))