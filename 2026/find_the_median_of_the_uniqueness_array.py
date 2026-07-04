"""
https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def median_of_uniqueness_array(self, nums: list[int]) -> int:
        """
        median of uniqueness array
        """
        def check(x: int) -> int:
            """
            find the number of subarrays with unique number at most x,
            using sliding window
            """
            rslt = 0
            cnt = Counter()
            start = 0
            for end, y in enumerate(nums):
                cnt[y] += 1
                while len(cnt) > x:
                    cnt[nums[start]] -= 1
                    if cnt[nums[start]] == 0:
                        del cnt[nums[start]]

                    start += 1

                rslt += end - start + 1

            return rslt

        n = len(nums)
        total_subarrays = (n * (n + 1)) >> 1
        l, r = 1, len(set(nums))
        while l < r:
            m = l + ((r - l) >> 1)
            if check(m) * 2 >= total_subarrays:
                r = m
            else:
                l = m + 1

        return l
