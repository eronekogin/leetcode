"""
https://leetcode.com/problems/sliding-subarray-beauty/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def get_subarray_beauty(self, nums: list[int], k: int, x: int) -> list[int]:
        """
        get subarray beauty
        """
        cnt = Counter()
        rslt: list[int] = []
        start = 0
        for end, num in enumerate(nums):
            if num < 0:
                cnt[num] += 1

            if end >= k - 1:
                rank = 0
                for y in sorted(cnt):
                    rank += cnt[y]
                    if rank >= x:
                        rslt.append(y)
                        break

                if rank < x:
                    rslt.append(0)

                if nums[start] < 0:
                    cnt[nums[start]] -= 1

                start += 1

        return rslt


print(Solution().get_subarray_beauty([-3, 1, 2, -3, 0, -3], 2, 1))
