"""
https://leetcode.com/problems/count-zero-request-servers/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def count_servers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        """
        count servers
        """
        cnt = Counter()
        start = end = used = 0
        logs.sort(key=lambda x: x[1])
        rslt: list[int] = [0] * len(queries)
        for t, i in sorted((t, i) for i, t in enumerate(queries)):
            while end < len(logs) and logs[end][1] <= t:
                cnt[logs[end][0]] += 1
                used += cnt[logs[end][0]] == 1
                end += 1

            while start < end and logs[start][1] + x < t:
                cnt[logs[start][0]] -= 1
                used -= cnt[logs[start][0]] == 0
                start += 1

            rslt[i] = n - used

        return rslt


print(Solution().count_servers(3, [[1, 3], [2, 6], [1, 5]], 5, [10, 11]))
