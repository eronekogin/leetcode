"""
https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def maximum_length(self, nums: list[int]) -> int:
        """
        maximum length
        """
        def check(x: int) -> int:
            if x == 1:
                return cnt[x] - (cnt[x] & 1 == 0)

            half_len = 0
            while cnt[x] >= 2:
                cnt[x] -= 2
                x = x ** 2
                half_len += 1

            half_len -= cnt[x] <= 0
            return 1 + (half_len << 1)

        cnt = Counter(nums)
        return max(
            check(x)
            for x in sorted(cnt.keys())
        )


print(Solution().maximum_length([5, 4, 1, 2, 2]))
