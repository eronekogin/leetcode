"""
https://leetcode.com/problems/maximum-binary-tree/
"""


from typing import List


from test_helper import TreeNode


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def do(start: int, end: int) -> TreeNode:
            if end < start:
                return None

            maxIdx, maxNum = start, nums[start]
            for i in range(start + 1, end + 1):
                if nums[i] > maxNum:
                    maxIdx, maxNum = i, nums[i]

            root = TreeNode(maxNum)
            root.left = do(start, maxIdx - 1)
            root.right = do(maxIdx + 1, end)
            return root

        return do(0, len(nums) - 1)

    def constructMaximumBinaryTree2(self, nums: List[int]) -> TreeNode:
        """
        Instead of finding the maximum number for each sub list every time, we
        simply use a stack which holds the numbers in descending order. Then
        we have:
            1. If the next number is less than the top of the stack, it is
                a candidate right node for the top of the stack, so we set it
                as the right node and also append it to the stack.
            2. Else, we keep popping from the stack until the stack is empty
                or the top of the stack is greater than the next number. Notice
                the last item popped from the stack will be the left node for
                the next number.
        """
        if not nums:
            return None

        stack = []
        for num in nums:
            node, lastPoppedNode = TreeNode(num), None
            while stack and stack[-1].val < num:
                lastPoppedNode = stack.pop()

            node.left = lastPoppedNode
            if stack:
                stack[-1].right = node

            stack.append(node)

        return stack[0]  # The first item in the stack is our root node.


print(Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5]))
