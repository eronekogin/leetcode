"""
https://leetcode.com/problems/count-the-number-of-good-subarrays/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def count_good(self, nums: list[int], k: int) -> int:
        """
        Every time we add a new number nums[j] to the sliding window,
        we add freqs[nums[j]] pairs, so we can check if we already have
        enough required pairs and reduce the current window until it
        has no sufficient pairs.

        Suppose at index i, the window has not enough pairs, then
        subarray i...j is not a good array, but for every index i2 < i,
        i2...j is a good array.
        """
        good_cnt = 0
        freqs = Counter()
        start = 0
        for x in nums:
            k -= freqs[x]
            freqs[x] += 1

            while k <= 0:
                freqs[nums[start]] -= 1
                k += freqs[nums[start]]
                start += 1

            good_cnt += start

        return good_cnt
