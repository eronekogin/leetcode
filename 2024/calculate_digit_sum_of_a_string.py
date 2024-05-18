"""
https://leetcode.com/problems/calculate-digit-sum-of-a-string/description/
"""


class Solution:
    """
    Solution
    """

    def digit_sum(self, s: str, k: int) -> str:
        """
        digit sum
        """
        if len(s) <= k:
            return s

        rslt = []
        cnt = 0
        for i, c in enumerate(s):
            if i >= k and i % k == 0:
                rslt.append(str(cnt))
                cnt = 0

            cnt += int(c)

        rslt.append(str(cnt))
        return self.digit_sum(''.join(rslt), k)


print(Solution().digit_sum("11111222223", 3))
