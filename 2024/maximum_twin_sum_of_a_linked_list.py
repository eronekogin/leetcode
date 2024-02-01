"""
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/
"""


from test_helper import ListNode


class Solution:
    """
    Solution
    """

    def pair_sum(self, head: ListNode) -> int:
        """
        pair_sum
        """
        nums: list[int] = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next

        n = len(nums)
        return max(nums[i] + nums[n - 1 - i] for i in range(n >> 1))
