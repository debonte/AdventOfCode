def getLinesFromFile(filePath: str) -> list[str]:
    with open(filePath, "r") as reader:
        return [x.strip() for x in reader.readlines()]