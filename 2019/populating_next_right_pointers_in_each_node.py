"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
"""


from test_helper import Node


class Solution:
    def connect(self, root: Node) -> Node:
        # Presumption: the input tree is a perfect binary tree.
        if not root:  # Empty tree.
            return None

        currNode = root
        while currNode.left:  # No need to check leaf level.
            nextNode = currNode
            while nextNode.next:
                nextNode.left.next = nextNode.right
                nextNode.right.next = nextNode.next.left
                nextNode = nextNode.next

            nextNode.left.next = nextNode.right  # Handle the rightmost node.
            currNode = currNode.left  # Go to the next level.

        return root


givenDict = {
    1: (2, 3),
    2: (4, 5),
    3: (6, 7)
}
root = Node(1)
root.create_tree(givenDict)
print(Solution().connect(root).print_tree())
