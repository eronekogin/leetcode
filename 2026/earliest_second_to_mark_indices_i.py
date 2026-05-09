"""
https://leetcode.com/problems/earliest-second-to-mark-indices-i/description/
"""


class Solution:
    """
    Solution
    """

    def earliest_second_to_mark_indices(self, nums: list[int], change_indices: list[int]) -> int:
        """
        earliest second to mark indices
        """
        def check(mid: int) -> bool:
            last_indices = [-1] * n
            for s in range(mid):
                last_indices[ci[s]] = s

            if last_indices[0] == -1:
                return False

            marked = 0
            capacity = 0

            for s in range(mid):
                if s == last_indices[ci[s]]:
                    if capacity >= nums[ci[s]]:
                        capacity -= nums[ci[s]]
                        marked += 1
                    else:
                        return False
                else:
                    capacity += 1

            return marked == n

        m = len(change_indices)
        n = len(nums)
        ci = [x - 1 for x in change_indices]
        l, r = 0, m + 1
        while l + 1 < r:
            mid = l + ((r - l) >> 1)
            if check(mid):
                r = mid
            else:
                l = mid

        if r == m + 1:
            return -1

        return r
