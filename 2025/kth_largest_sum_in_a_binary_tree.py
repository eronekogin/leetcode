"""
https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description/
"""


from heapq import heappop, heappush

from test_helper import TreeNode


class Solution:
    """
    Solution
    """

    def kth_largest_level_sum(self, root: TreeNode, k: int) -> int:
        """
        kth largest level sum
        """
        sum_heap: list[int] = []
        curr_nodes = [root]
        while curr_nodes:
            curr_sum = 0
            next_nodes: list[TreeNode] = []
            for node in curr_nodes:
                curr_sum += node.val
                if node.left:
                    next_nodes.append(node.left)

                if node.right:
                    next_nodes.append(node.right)

            curr_nodes = next_nodes
            heappush(sum_heap, curr_sum)

            if len(sum_heap) > k:
                heappop(sum_heap)

        if len(sum_heap) < k:
            return -1

        return sum_heap[0]
