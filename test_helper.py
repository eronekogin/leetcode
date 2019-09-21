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
        return '{0} -> ({1}, {2})'.format(self.val, self.left, self.right)

    def create_tree(self, givenDict: Dict[int, Tuple[int, int]]) -> None:
        nodeList, nextList = [self], []
        while nodeList:
            for node in nodeList:
                left, right = givenDict.get(node.val, [None, None])
                if left:
                    node.left = TreeNode(left)
                    nextList.append(node.left)

                if right:
                    node.right = TreeNode(right)
                    nextList.append(node.right)

            nodeList = nextList
            nextList = []
