"""
https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/
"""


from typing import List


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self, root: TreeNode):
        self.root = root

    def insert(self, newNode: TreeNode) -> None:
        """
        Insert a new node to the BST.
        """
        currNode = self.root
        while currNode:
            if currNode.val > newNode.val:
                if currNode.left:
                    currNode = currNode.left
                else:
                    currNode.left = newNode
                    break
            else:
                if currNode.right:
                    currNode = currNode.right
                else:
                    currNode.right = newNode
                    break

    def ceiling(self, val: int) -> int:
        """
        Try to find a node in BST whose value is the minimum value that is
        not less than the input value, then return the node's value.
        """
        currNode = self.root
        rslt = float('inf')
        while currNode:
            if currNode.val < val:
                currNode = currNode.right
            else:
                rslt = min(rslt, currNode.val)
                currNode = currNode.left

        return rslt


class Solution:
    def _get_limit_max_sub_sum(self, nums: List[int], k: int) -> int:
        """
        Try to find a contiguous sub list from nums whose summary <= k.
        The search process is accelarated by storing the pre calculated
        sub summaries to each node of a BST.
        """
        currSum, currMax = 0, float('-inf')
        bst = BST(TreeNode(currSum))
        for num in nums:
            currSum += num
            preSum = bst.ceiling(currSum - k)
            currMax = max(currMax, currSum - preSum)
            bst.insert(TreeNode(currSum))

        return currMax

    def _get_no_limit_max_sub_sum(self, nums: List[int]) -> int:
        """
        Get the maximum summary of any contiguous sub list from the input list.
        """
        currMax, currSum = float('-inf'), 0
        for num in nums:
            currSum = max(num, currSum + num)
            currMax = max(currMax, currSum)

        return currMax

    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """
        Presumptions:
        1. matrix is not empty.
        2. matrix has more rows than columns.
        """
        R, C = len(matrix), len(matrix[0])
        currMax = float('-inf')
        for c1 in range(C):
            rowSums = [0] * R
            for c2 in range(c1, C):
                # First calculate sum between column c1 to c2 of each row.
                for r in range(R):
                    rowSums[r] += matrix[r][c2]

                # Then the sum of rectangles between column c1 and c2
                # could be formed by any contiguous sub list from rowSums.
                # So firstly we try to get the maximum sub sum from rowSums.
                noLimitSubMax = self._get_no_limit_max_sub_sum(rowSums)
                if noLimitSubMax <= k:
                    currMax = max(currMax, noLimitSubMax)
                else:
                    currMax = max(
                        currMax, self._get_limit_max_sub_sum(rowSums, k))

                # Found the maximum possible sub sum.
                if currMax == k:
                    return k

        return currMax


print(Solution().maxSumSubmatrix([[1, 0, 1], [0, -2, 3]], 2))
