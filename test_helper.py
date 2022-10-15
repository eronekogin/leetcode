class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None

    def __repr__(self):
        nextVal = self.next.val if self.next else None
        return '{0} -> {1}'.format(self.val, nextVal)

    def create_node_list(
            self, start: int | None = None,
            stop: int | None = None,
            givenList: list[int] | None = None) -> 'ListNode':
        temp = self
        if givenList is None:
            if start is None or stop is None:
                return self

            for i in range(start, stop):
                temp.next = ListNode(i)
                temp = temp.next
        else:
            for i in givenList:
                temp.next = ListNode(i)
                temp = temp.next

        return self

    def create_cycle_list(
            self, givenList: list[int], cyclePos: int) -> 'ListNode':
        currNode, currList = self, []
        for i in givenList:
            currNode.next = ListNode(i)
            currList.append(currNode.next)
            currNode = currNode.next

        currNode.next = currList[cyclePos]
        return self

    def print_single_list(self) -> list[int]:
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

    def create_tree(self, givenDict: dict[int, tuple[int | None, int | None]]):
        nodes = [self]
        while nodes:
            nextNodes = []
            for node in nodes:
                left, right = givenDict.get(node.val, (None, None))
                if left is not None:
                    node.left = TreeNode(left)
                    nextNodes.append(node.left)

                if right is not None:
                    node.right = TreeNode(right)
                    nextNodes.append(node.right)

            nodes = nextNodes

        return self

    def print_tree(self) -> dict[int, tuple[int, int]]:
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

    def create_tree(self, givenDict: dict[int, tuple[int, int]]):
        nodes = [self]
        while nodes:
            nextNodes = []
            for node in nodes:
                left, right = givenDict.get(node.val, (None, None))
                if left is not None:
                    node.left = Node(left)
                    nextNodes.append(node.left)

                if right is not None:
                    node.right = Node(right)
                    nextNodes.append(node.right)

            nodes = nextNodes

    def print_tree(self) -> dict[int, tuple[int, int, int]]:
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
    def __init__(self, val: int, neighbors: list['GraphNode']):
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
    def __init__(self, num: int | None = None):
        if num is None:
            self.num = None
            self.nestedList = []
        else:
            self.num = num
            self.nestedList = None

    def isInteger(self) -> bool:
        return self.nestedList is None

    def getInteger(self) -> int | None:
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

    def getList(self) -> list['NestedInteger']:
        if self.nestedList is not None:
            return self.nestedList

        return [self]

    def __repr__(self) -> str:
        if self.nestedList is None:
            return str(self.num)
        else:
            return str(self.nestedList)


class QuadTreeNode:
    def __init__(
            self,
            val: bool,
            isLeaf: bool,
            topLeft: 'QuadTreeNode',
            topRight: 'QuadTreeNode',
            bottomLeft: 'QuadTreeNode',
            bottomRight: 'QuadTreeNode'):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class NaryTreeNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class DoublyLinkedListNode:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Employee:
    def __init__(self, id: int, importance: int, subordinates: list[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class MountainArray:
    def __init__(self, items: list[int]) -> None:
        self.items = items

    def get(self, index: int) -> int:
        return self.items[index]

    def length(self) -> int:
        return len(self.items)
