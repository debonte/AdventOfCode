from typing import Tuple

# First thing I tried was creating a tree from the input string, but then finding
# the left and right spots for exploding wasn't obvious to me.
# This new approach is getting painful too.
# I think I could simplify it by creating a tokenizer that turns the string into a
# stream of tokens, primarily to handle the multi-digit integer case.


def reduce(input: str) -> str:
    depth = 0
    for i in range(0, len(input)):
        ch = input[i]

        if ch == "[":
            depth += 1

            if depth >= 4 and isRegularNumberPair(input[i:]):
                (left, right) = parseRegularNumberPair(input[i:])

                for leftSearch in range(i, 0, -1):
                    if isDigit(input[leftSearch]):
                        end = leftSearch
                        for leftSearch in range(leftSearch, 0, -1):
                            if not isDigit(input[leftSearch]):
                                start = leftSearch + 1

                                value = int(input[start:end-start+1]) + left

                for rightSearch
                        

        elif ch == "]":
            depth -= 1
        elif ch == ",":
            pass
        else:
            pass


def isRegularNumberPair(input: str) -> bool:
    try:
        parseRegularNumberPair(input)
        return True
    except:
        return False


def parseRegularNumberPair(input: str) -> Tuple[int, int]:
    if input[0] != "[":
        raise ValueError()
    
    i = 1
    leftStart = i
    while i < len(input) and isDigit(input[i]):
        i += 1

    left = int(input[leftStart:i-leftStart])

    if input[i] != ",":
        raise ValueError()
    
    i += 1
    rightStart = i
    while i < len(input) and isDigit(input[i]):
        i += 1

    right = int(input[rightStart:i-rightStart])

    if input[i] != "]":
        raise ValueError()

    return (left, right)


def isDigit(ch: str) -> bool:
    return ch == "0" or ch == "1" or ch == "2" or ch == "3" or ch == "4" or ch == "5" or ch == "6" or ch == "7" or ch == "8" or ch == "9"

# class SnailfishTreeNode:
#     pass

# class SnailfishTreeParentNode(SnailfishTreeNode):
#     def __init__(self, left: SnailfishTreeNode, right: SnailfishTreeNode):
#         self.left = left
#         self.right = right

# class SnailfishTreeLeafNode(SnailfishTreeNode):
#     def __init__(self, value: int):
#         self.value = value

# def parseNumber(serializedTree: str) -> Tuple[SnailfishTreeNode, int]:
#     endIndex = 0

#     while serializedTree[endIndex].isdigit():
#         endIndex += 1

#     number = int(serializedTree[0:endIndex])
#     return (SnailfishTreeLeafNode(number), endIndex)

# def parsePair(serializedTree: str) -> Tuple[SnailfishTreeNode, int]:
#     if serializedTree[0] != "[":
#         raise BaseException()

#     index = 1
#     if serializedTree[index] == '[':
#         (leftNode, charsConsumed) = parsePair(serializedTree[1:])
#     else:
#         (leftNode, charsConsumed) = parseNumber(serializedTree[1:])

#     index += charsConsumed
#     if serializedTree[index] != ",":
#         raise BaseException()

#     index += 1
#     if serializedTree[index] == '[':
#         (rightNode, charsConsumed) = parsePair(serializedTree[index:])
#     else:
#         (rightNode, charsConsumed) = parseNumber(serializedTree[index:])

#     index += charsConsumed
#     if serializedTree[index] != "]":
#         raise BaseException()

#     return (SnailfishTreeParentNode(leftNode, rightNode), index + 1)

# def parse(serializedTree: str) -> SnailfishTreeNode | None:
#     (root, _) = parsePair(serializedTree)
#     return root

# tree = reduce("[1,2]")
# tree = reduce("[[1,2],3]")
# tree = reduce("[9,[8,7]]")
# tree = reduce("[[1,9],[8,5]]")
# tree = reduce("[[[[1,2],[3,4]],[[5,6],[7,8]]],9]")
# tree = reduce("[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]")
# tree = reduce("[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]")

# def depthFirstSearch(root: SnailfishTreeNode) -> Iterator[Tuple[SnailfishTreeNode, int]]:
#     current = root
#     depth = 0
#     stack: list[SnailfishTreeNode] = list()

#     while current != None:
#         yield (current, depth)
#         if isinstance(current, SnailfishTreeParentNode): 
#             stack.append(current.right)
#             current = current.left
#             depth += 1
#         else:
#             current = stack.pop() if len(stack) > 0 else None
#             depth -= 1


# def reduce(root: SnailfishTreeNode) -> SnailfishTreeNode:
#     for (node, depth) in depthFirstSearch(root):
#         if depth >= 4:
#             # explode
#         else if isinstance(node, SnailfishTreeLeafNode) and node.value >= 10:
#             # split
