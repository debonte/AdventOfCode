from typing import Union


def loadFile(filePath: str) -> list[str]:
    with open(filePath, "r") as reader:
        return [x.strip() for x in reader.readlines()]

Packet = list[Union[int, "Packet"]]

def parsePacket(packet: str) -> Packet:
    result = Packet()

    # skip [
    i = 1

    while i < len(packet):
        if packet[i] == "[":
            subpacket = parsePacket(packet[i:])
            result.append(subpacket)
        elif packet[i] == "]":
            break
        else:
            end = i + 1
            while packet[end] != "," and packet[end] != "]":
                end += 1

            number = int(packet[i:end])
            result.append(number)

    return result
    

def inOrder(left: Packet, right: Packet) -> bool | None:
    if len(left) == 0 and len(right) > 0:
        return True
    
    if len(right) == 0:
        return False

    for i in range(len(left)):
        leftElement = left[i]
        rightElement = right[i]

        if isinstance(leftElement, int) and isinstance(rightElement, int):
            if leftElement < rightElement:
                return True
            elif leftElement > rightElement:
                return False
        
        elif isinstance(leftElement, list) and isinstance(rightElement, list):
            correct = inOrder(leftElement, rightElement)
            if correct != None:
                return correct

        else:
            if isinstance(leftElement, int):
                leftElement = [leftElement]
            else:
                rightElement = [rightElement]

            correct = inOrder(leftElement, rightElement)
            if correct != None:
                return correct
  
    return None


def part1(input: list[str]) -> int:
    i = 0
    result = 0

    while i < len(input):
        left = parsePacket(input[i])
        right = parsePacket(input[i + 1])

        if inOrder(left, right):
            result += 1

        i += 3

    return result

input = loadFile("Data\\Day13Example.txt")
print(part1(input))