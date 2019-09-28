from typing import List, Dict, Tuple


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None

    def __repr__(self):
        return '{0} -> {1}'.format(self.val, self.next)

    def create_node_list(
            self, start: int = None,
            stop: int = None, givenList: List[int] = None) -> 'ListNode':
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


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        left = self.left.val if self.left else None
        right = self.right.val if self.right else None
        return '{0} -> ({1}, {2})'.format(self.val, left, right)

    def create_tree(self, givenDict: Dict[int, Tuple[int, int]]) -> None:
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
