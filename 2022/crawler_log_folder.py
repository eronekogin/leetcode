"""
https://leetcode.com/problems/crawler-log-folder/
"""


class Solution:
    def minOperations(self, logs: list[str]) -> int:
        depth = 0
        for action in logs:
            if action == '../':
                depth = max(0, depth - 1)
            elif action != './':
                depth += 1

        return depth


print(Solution().minOperations(["d1/", "d2/", "../", "d21/", "./"]))
