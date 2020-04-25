from typing import List, Dict, Tuple


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None

    def __repr__(self):
        nextVal = self.next.val if self.next else None
        return '{0} -> {1}'.format(self.val, nextVal)

    def create_node_list(
            self, start: int = None,
            stop: int = None,
            givenList: List[int] = None) -> 'ListNode':
        temp = self
        if givenList is None:
            for i in range(start, stop):
                temp.next = ListNode(i)
                temp = temp.next
        else:
            for i in givenList:
                temp.next = ListNode(i)
                temp = temp.next

        return self.next

    def create_cycle_list(
            self, givenList: List[int], cyclePos: int) -> 'ListNode':
        currNode, currList = self, []
        for i in givenList:
            currNode.next = ListNode(i)
            currList.append(currNode.next)
            currNode = currNode.next

        currNode.next = currList[cyclePos]
        return self.next

    def print_single_list(self) -> List[int]:
        currNode, rslt = self, []
        while currNode:
            rslt.append(currNode.val)
            currNode = currNode.next

        return rslt


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        left = self.left.val if self.left else None
        right = self.right.val if self.right else None
        return '{0} -> ({1}, {2})'.format(self.val, left, right)

    def create_tree(self, givenDict: Dict[int, Tuple[int, int]]):
        nodes = [self]
        while nodes:
            nextNodes = []
            for node in nodes:
                left, right = givenDict.get(node.val, (None, None))
                if left:
                    node.left = TreeNode(left)
                    nextNodes.append(node.left)

                if right:
                    node.right = TreeNode(right)
                    nextNodes.append(node.right)

            nodes = nextNodes

    def print_tree(self) -> Dict[int, Tuple[int, int]]:
        nodes, rslt = [self], {}
        while nodes:
            nextNodes = []
            for node in nodes:
                left, right = None, None
                if node.left:
                    left = node.left.val
                    nextNodes.append(node.left)

                if node.right:
                    right = node.right.val
                    nextNodes.append(node.right)

                rslt[node.val] = (left, right)

            nodes = nextNodes

        return rslt


class Node(TreeNode):
    def __init__(self, x: int):
        super().__init__(x)
        self.next = None

    def __repr__(self):
        return '{0}, next: {1}'.format(super().__repr__(), self.next)

    def create_tree(self, givenDict: Dict[int, Tuple[int, int]]):
        nodes = [self]
        while nodes:
            nextNodes = []
            for node in nodes:
                left, right = givenDict.get(node.val, (None, None))
                if left:
                    node.left = Node(left)
                    nextNodes.append(node.left)

                if right:
                    node.right = Node(right)
                    nextNodes.append(node.right)

            nodes = nextNodes

    def print_tree(self) -> Dict[int, Tuple[int, int, int]]:
        nodes, rslt = [self], {}
        while nodes:
            nextNodes = []
            for node in nodes:
                left, right, nxt = None, None, None
                if node.left:
                    left = node.left.val
                    nextNodes.append(node.left)

                if node.right:
                    right = node.right.val
                    nextNodes.append(node.right)

                if node.next:
                    nxt = node.next.val

                rslt[node.val] = (left, right, nxt)

            nodes = nextNodes

        return rslt


class GraphNode:
    def __init__(self, val: int, neighbors: List['GraphNode']):
        self.val = val
        self.neighbors = neighbors


class RandomNode:
    def __init__(self, val: int, next: 'RandomNode', random: 'RandomNode'):
        self.val = val
        self.next = next
        self.random = random

    def __repr__(self):
        next = self.next.val if self.next else None
        random = self.random.val if self.random else None
        return '{0}: (next: {1}, random: {2})'.format(self.val, next, random)


class NestedInteger:
    def __init__(self, num: int = None):
        if num is None:
            self.num = None
            self.nestedList = []
        else:
            self.num = num
            self.nestedList = None

    def isInteger(self) -> bool:
        return self.nestedList is None

    def getInteger(self) -> int:
        if self.num is not None:
            return self.num

    def add(self, elem: 'NestedInteger'):
        if self.nestedList is None:
            self.num = None
            self.nestedList = []

        self.nestedList.append(elem)

    def setInteger(self, value: int):
        self.num = value
        self.nestedList = None

    def getList(self) -> List['NestedInteger']:
        if self.nestedList is not None:
            return self.nestedList

    def __repr__(self) -> str:
        if self.nestedList is None:
            return str(self.num)
        else:
            return str(self.nestedList)
