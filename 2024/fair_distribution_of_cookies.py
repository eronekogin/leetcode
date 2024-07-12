"""
https://leetcode.com/problems/fair-distribution-of-cookies/description/
"""


class Solution:
    """
    Solution
    """

    def distribute_cookies(self, cookies: list[int], k: int) -> int:
        """
        distribute cookies
        """
        def dfs(i: int, zero_cnt: int) -> int:
            if i + zero_cnt > n:  # Not enough cookie to distribute
                return 10 ** 7

            if i == n:
                return max(curr)

            rslt = 10 ** 7
            for j in range(k):
                zero_cnt -= curr[j] == 0
                curr[j] += cookies[i]

                rslt = min(rslt, dfs(i + 1, zero_cnt))

                curr[j] -= cookies[i]
                zero_cnt += curr[j] == 0

            return rslt

        curr = [0] * k
        n = len(cookies)
        return dfs(0, k)
