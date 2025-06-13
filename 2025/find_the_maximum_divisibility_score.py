"""
https://leetcode.com/problems/find-the-maximum-divisibility-score/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def max_div_score(self, nums: list[int], divisors: list[int]) -> int:
        """
        max div score
        """
        max_divisor, max_score = -1, -1
        cnt = Counter(nums)
        for d in sorted(set(divisors)):
            curr_score = sum(cnt[x] for x in cnt if x % d == 0)
            if curr_score > max_score:
                max_divisor, max_score = d, curr_score

        return max_divisor
