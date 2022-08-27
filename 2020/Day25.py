cardPublicKey = 13316116
doorPublicKey = 13651422

def getLoopSize(target):
    value = 1
    SUBJECT = 7
    loopSize = 0

    while value != target:
        value = value * SUBJECT
        value = value % 20201227
        loopSize = loopSize + 1
    
    return loopSize

def transform(subject, loopSize):
    value = 1
    for i in range(0, loopSize):
        value = value * subject
        value = value % 20201227

    return value

cardSecretLoopSize = getLoopSize(cardPublicKey)
doorSecretLoopSize = getLoopSize(doorPublicKey)

print(transform(doorPublicKey, cardSecretLoopSize))
print(transform(cardPublicKey, doorSecretLoopSize))
