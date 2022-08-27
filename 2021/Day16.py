from typing import Tuple


def convertHexToBinary(hexString: str) -> str:
    binaryString = ""
    for ch in hexString:
        binaryString += bin(int(ch, 16))[2:].zfill(4)
    return binaryString


def readPacketFromFile(filePath: str = "Data\\Day16.txt") -> str:
    with open(filePath, "r") as reader:
        hexString = reader.readline().strip()
        print(hexString)
        return convertHexToBinary(hexString)


def getIntegerValue(binaryString: str) -> int:
    result = 0
    for ch in binaryString:
        result = result * 2 + int(ch)
    return result


def getSumOfVersions(packet: str) -> Tuple[int, int]:
    version = getIntegerValue(packet[0:3])
    typeId = getIntegerValue(packet[3:6])
    print(f"Version: {version}, TypeId: {'Literal' if typeId == 4 else 'Operator'}")

    if typeId == 4:
        nextPrefixBit = 6
        while packet[nextPrefixBit] != "0":
            nextPrefixBit += 5
        return (version, nextPrefixBit + 5)
    else:
        lengthTypeId = getIntegerValue(packet[6:7])

        length = 0
        numSubPackets = 0
        if lengthTypeId == 0:
            length = getIntegerValue(packet[7:22])
            nextPacketStart = 22
        else:
            numSubPackets = getIntegerValue(packet[7:18])
            nextPacketStart = 18

        result = version
        bytesConsumed = 0
        subpacketsConsumed = 0
        while True:
            (subpacketVersion, subpacketLength) = getSumOfVersions(
                packet[nextPacketStart:]
            )
            result += subpacketVersion
            bytesConsumed += subpacketLength
            subpacketsConsumed += 1
            nextPacketStart += subpacketLength

            if length > 0:
                if bytesConsumed >= length:
                    break
            else:
                if subpacketsConsumed >= numSubPackets:
                    break

        return (result, nextPacketStart)


def getValue(packet: str) -> Tuple[int, int]:
    version = getIntegerValue(packet[0:3])
    typeId = getIntegerValue(packet[3:6])
    print(f"Version: {version}, TypeId: {'Literal' if typeId == 4 else 'Operator'}")

    if typeId == 4:
        nextPrefixBit = 6
        binaryValue = ""
        while True:
            binaryValue += packet[nextPrefixBit + 1 : nextPrefixBit + 5]
            if packet[nextPrefixBit] == "0":
                break
            nextPrefixBit += 5

        return (getIntegerValue(binaryValue), nextPrefixBit + 5)
    else:
        lengthTypeId = getIntegerValue(packet[6:7])

        length = 0
        numSubPackets = 0
        if lengthTypeId == 0:
            length = getIntegerValue(packet[7:22])
            nextPacketStart = 22
        else:
            numSubPackets = getIntegerValue(packet[7:18])
            nextPacketStart = 18

        subpacketValues = list()
        result = version
        bytesConsumed = 0
        subpacketsConsumed = 0
        while True:
            (subpacketValue, subpacketLength) = getValue(packet[nextPacketStart:])
            subpacketValues.append(subpacketValue)
            bytesConsumed += subpacketLength
            subpacketsConsumed += 1
            nextPacketStart += subpacketLength

            if length > 0:
                if bytesConsumed >= length:
                    break
            else:
                if subpacketsConsumed >= numSubPackets:
                    break

        if typeId == 0:
            result = sum(subpacketValues)
        elif typeId == 1:
            result = subpacketValues[0]
            for subpacketValue in subpacketValues[1:]:
                result *= subpacketValue
        elif typeId == 2:
            result = min(subpacketValues)
        elif typeId == 3:
            result = max(subpacketValues)
        elif typeId == 5:
            result = 1 if subpacketValues[0] > subpacketValues[1] else 0
        elif typeId == 6:
            result = 1 if subpacketValues[0] < subpacketValues[1] else 0
        elif typeId == 7:
            result = 1 if subpacketValues[0] == subpacketValues[1] else 0

        return (result, nextPacketStart)


packet = readPacketFromFile("Data\\Day16.txt")
print(packet)
print(getValue(packet))
