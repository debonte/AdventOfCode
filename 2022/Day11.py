from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Literal

@dataclass
class Monkey:
    items: list[int]
    operation: Literal["+"] | Literal["*"]
    operationFactor: int
    testDivisibility: int
    testTrueMonkey: int
    testFalseMonkey: int
    inspections: int = field(default=0, init=False)

def loadFile(filePath: str) -> list[Monkey]:
    with open(filePath, "r") as reader:
        lines = [x.strip() for x in reader.readlines()]

        iLine = 0
        numMonkeys = int((len(lines) + 1) / 7)
        monkeys = []

        for _ in range(numMonkeys):
            # Skip Monkey header
            iLine += 1

            # Read items
            items = [int(x) for x in lines[iLine][16:].split(", ")]
            iLine += 1

            # Read operation
            operation = lines[iLine][21:22]
            if operation != "+" and operation != "*":
                raise Exception("Invalid operation")
            factor = lines[iLine][23:]
            operationFactor = -1 if factor == "old" else int(factor) 
            iLine += 1

            # Read test
            testDivisibility = int(lines[iLine][19:])
            iLine += 1
            trueTarget = int(lines[iLine][25:])
            iLine += 1
            falseTarget = int(lines[iLine][26:])

            # Skip blank line
            iLine += 2

            monkeys.append(Monkey(items, operation, operationFactor, testDivisibility, trueTarget, falseTarget))

        return monkeys

def round(monkeys: list[Monkey], worryDivisor: int):
    simplifier = 1
    for monkey in monkeys:
        simplifier *= monkey.testDivisibility

    for monkey in monkeys:
        while len(monkey.items) > 0:
            item = monkey.items.pop(0)

            factor = monkey.operationFactor
            if factor == -1:
                factor = item

            if monkey.operation == "+":
                worry = item + factor
            else:
                worry = item * factor

            if worryDivisor != 1:
                worry = int(worry / worryDivisor)

            worry %= simplifier

            if worry % monkey.testDivisibility == 0:
                monkeys[monkey.testTrueMonkey].items.append(worry)
            else:
                monkeys[monkey.testFalseMonkey].items.append(worry)

            monkey.inspections += 1


def run(monkeys: list[Monkey], worryDivisor: int, rounds: int):
    for _ in range(rounds):
        round(monkeys, worryDivisor)

    inspections = [monkey.inspections for monkey in monkeys]
    topTwo = sorted(inspections)[-2:]

    return topTwo[0] * topTwo[1]

input = loadFile("Data\\Day11.txt")
print(run(input, 3, 20))
print(run(input, 1, 10000))
