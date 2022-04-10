"""
https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
"""


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1  # Total empty slots to hold the nodes of the tree.
        for currNode in preorder.split(','):
            if not slots:  # No more empty slot to hold a new tree node.
                return False

            if currNode == '#':
                # A null node only takes one slot.
                slots -= 1
            else:
                # A not-null node takes one slot and creates two more slots.
                slots += 1

        return not slots  # In the end there should be no empty slot left.
