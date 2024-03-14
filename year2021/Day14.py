class Rule:
    pair: str
    insert: str

    def __init__(self, pair: str, insert: str):
        self.pair = pair
        self.insert = insert

    @staticmethod
    def parse(string: str):
        pair = string[0:2]
        insert = string[6:7]
        return Rule(pair, insert)

class Instructions:
    template: str
    rules: dict[str, str]

    def __init__(self, template: str, rules: dict[str, str]):
        self.template = template
        self.rules = rules

def loadFile(filePath: str = "Data\\Day14.txt") -> Instructions:
    with open(filePath, "r") as reader:
        template = reader.readline().strip()
        reader.readline()
        rules = [Rule.parse(line.strip()) for line in reader.readlines()]
        ruleMap = {rule.pair: rule.insert for rule in rules}
        return Instructions(template, ruleMap)

def applyRulesOnce(counts: dict[str, int], rules: dict[str, str]) -> dict[str, int]:
    newCounts = counts.copy()
    for pair in counts:
        insert = rules[pair]
        pairCount = counts[pair]
        if pairCount == 0:
            continue
            
        firstNewPair = pair[0] + insert
        secondNewPair = insert + pair[1]
        newCounts[pair] -= pairCount
        newCounts[firstNewPair] += pairCount
        newCounts[secondNewPair] += pairCount
    return newCounts

def applyRules(template: str, rules: dict[str, str], applyCount: int) -> dict[str, int]:
    counts = {pair: 0 for pair in rules}
    for i in range(len(template) - 1):
        pair = template[i:i+2]
        counts[pair] += 1

    for i in range(applyCount):
        counts = applyRulesOnce(counts, rules)
    return counts

def getAnswer(originalTemplate: str, counts: dict[str, int]) -> int:
    letterCounts = { "A" : 0, "B" : 0, "C" : 0, "D" : 0, "E" : 0, "F" : 0, "G" : 0, "H" : 0, "I" : 0, "J" : 0, "K" : 0, "L" : 0, "M" : 0, "N" : 0, "O" : 0, "P" : 0, "Q" : 0, "R" : 0, "S" : 0, "T" : 0, "U" : 0, "V" : 0, "W" : 0, "X" : 0, "Y" : 0, "Z" : 0 }
    for pair in counts:
        pairCount = counts[pair]
        letterCounts[pair[0]] += pairCount 
        letterCounts[pair[1]] += pairCount

    # First and last letter of template never change and they're the only ones that
    # are not double counted by the calculation above
    letterCounts[originalTemplate[0]] += 1
    letterCounts[originalTemplate[len(originalTemplate) - 1]] += 1

    mostCommonCount = max(letterCounts.values()) / 2
    leastCommonCount = min([value for value in letterCounts.values() if value > 0]) / 2
    return mostCommonCount - leastCommonCount
    
instructions = loadFile()
result = applyRules(instructions.template, instructions.rules, 40)
print(getAnswer(instructions.template, result))