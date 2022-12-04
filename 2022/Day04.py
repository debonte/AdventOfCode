def loadFile(filePath: str) -> int:
    with open(filePath, "r") as reader:
        lines = [x.strip() for x in reader.readlines()]

        fullOverlap = 0
        anyOverlap = 0
        for line in lines:
            (range1, range2) = line.split(",")
            
            (start, end) = range1.split("-")
            range1Start = int(start)
            range1End = int(end)
            
            (start, end) = range2.split("-")
            range2Start = int(start)
            range2End = int(end)

            if (range1Start >= range2Start and range1End <= range2End) or (range2Start >= range1Start and range2End <= range1End):
               fullOverlap += 1

            if (range1Start >= range2Start and range1Start <= range2End) or\
               (range1End >= range2Start and range1End <= range2End) or\
               (range2Start >= range1Start and range2Start <= range1End) or\
               (range2End >= range1Start and range2End <= range1End):
               anyOverlap += 1

        return anyOverlap

print(loadFile("Data\\Day04.txt"))