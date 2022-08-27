from collections import deque
from operator import contains
from typing import Container, Tuple
from typing_extensions import Self

class Node:
    name: str
    neighbors: set[Self]

    def __init__(self, name: str):
        self.name = name
        self.neighbors = set()

    def isSmallCave(self) -> bool:
        return self.name[0].islower()

    def isLargeCave(self) -> bool:
        return not self.isSmallCave()

    def __repr__(self) -> str:
        return self.name

        
class Path(Container[Node]):
    nodes: list[Node]
    hasSmallCaveBeenVisitedTwice: bool = False

    def __init__(self):
        self.nodes = []

    def canVisit(self, node: Node) -> bool:
        if node.isLargeCave():
            return True

        alreadyVisited = contains(self, node)
        if not alreadyVisited:
            return True
        
        if node.name == "start" or node.name == "end":
            return False

        return not self._hasSmallCaveBeenVisitedTwice()

    def add(self, node: Node):
        if node.isSmallCave() and contains(self, node):
            self.hasSmallCaveBeenVisitedTwice = True

        self.nodes.append(node)

    def copyAndAdd(self, node: Node) -> Self:
        copy = Path()
        copy.nodes = self.nodes.copy()
        copy.hasSmallCaveBeenVisitedTwice = self.hasSmallCaveBeenVisitedTwice
        copy.add(node)
        return copy

    def tail(self) -> Node:
        return self.nodes[-1]
    
    def _hasSmallCaveBeenVisitedTwice(self) -> bool:
        return self.hasSmallCaveBeenVisitedTwice

    def __contains__(self, node: object) -> bool:
        return contains(self.nodes, node)

    def __repr__(self) -> str:
        return ",".join([node.name for node in self.nodes])



def getOrCreateNode(nodes: dict[str, Node], name: str) -> Node:
    if contains(nodes, name):
        return nodes[name]
    
    node = Node(name)
    nodes[name] = node
    return node


def loadFile(filePath: str = "Data\\Day12.txt") -> Tuple[Node, Node]:
    with open(filePath, "r") as reader:
        nodes: dict[str, Node] = dict()

        for line in reader.readlines():
            (startName, endName) = line.split("-")
            startName = startName.strip()
            endName = endName.strip()

            startNode = getOrCreateNode(nodes, startName)
            endNode = getOrCreateNode(nodes, endName)

            startNode.neighbors.add(endNode)
            endNode.neighbors.add(startNode)

        return (nodes["start"], nodes["end"])

        
def getPathCount(startNode: Node, endNode: Node) -> int:
    root = Path()
    root.add(startNode)

    queue: deque[Path] = deque()
    queue.append(root)

    completePaths: list[Path] = []

    while queue:
        path = queue.pop()
        for neighbor in path.tail().neighbors:
            if path.canVisit(neighbor):
                copy = path.copyAndAdd(neighbor)
                if (neighbor == endNode):
                    completePaths.append(copy)
                else:
                    queue.append(copy)

    # for path in completePaths:
    #     print(path)

    return len(completePaths)

            
(startNode, endNode) = loadFile()
print(getPathCount(startNode, endNode))