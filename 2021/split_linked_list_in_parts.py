"""
https://leetcode.com/problems/split-linked-list-in-parts/
"""


from typing import List


from test_helper import ListNode


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        if not root:
            return [None] * k

        # First calculate the total length of the list.
        currNode, total = root, 0
        while currNode:
            total += 1
            currNode = currNode.next

        partLen, remainLen = divmod(total, k)
        currNode, rslt, partCnt = root, [], 0
        for partCnt in range(k):  # Split list to parts with partLen length.
            rslt.append(currNode)
            for _ in range(partLen + (partCnt < remainLen)):
                preNode, currNode = currNode, currNode.next

            preNode.next = None

        return rslt


root = ListNode(1)
root.create_node_list(1, 11)
print(Solution().splitListToParts(root.next, 3))
