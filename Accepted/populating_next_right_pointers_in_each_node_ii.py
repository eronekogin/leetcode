"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
"""


from test_helper import Node


class Solution:
    def connect(self, root: Node) -> Node:
        currParent = root
        currChild = nextDummyHead = Node(None)
        while currParent:
            if currParent.left:
                currChild.next = currParent.left
                currChild = currChild.next

            if currParent.right:
                currChild.next = currParent.right
                currChild = currChild.next

            if currParent.next:
                currParent = currParent.next
            else:
                # Arrived at the end of the current level.
                # Now go to the next level.
                currParent = nextDummyHead.next
                nextDummyHead.next = None
                currChild = nextDummyHead

        return root


givenDict = {
    1: (2, 3),
    3: (4, 6),
    4: (None, 5),
    6: (7, None)
}
root = Node(1)
root.create_tree(givenDict)
print(Solution().connect(root).print_tree())
