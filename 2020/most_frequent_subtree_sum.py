"""
https://leetcode.com/problems/most-frequent-subtree-sum/
"""


from typing import List

from test_helper import TreeNode


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        def calc_sum(curr: TreeNode) -> int:
            if not curr:
                return 0

            currSum = curr.val + calc_sum(curr.left) + calc_sum(curr.right)
            sumMemo[currSum] = sumMemo.get(currSum, 0) + 1
            return currSum

        if not root:
            return []

        sumMemo = {}  # {subTree sum: frequency}
        calc_sum(root)

        # Determine the most frequent sum.
        maxSum = max(sumMemo.values())
        return [k for k in sumMemo if sumMemo[k] == maxSum]
