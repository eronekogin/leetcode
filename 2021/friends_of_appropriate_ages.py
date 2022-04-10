"""
https://leetcode.com/problems/friends-of-appropriate-ages/
"""


from collections import Counter


class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        """
        For each a, b in the counter of ages:
        1. If a != b, request(a, b) will make cnt[a] * cnt[b] friends.
        2. If a == b, request(a, b) will make cnt[a] * (cnt[a] - 1) friends.
        """
        def request(a: int, b: int) -> bool:
            return not (b > a or b <= a / 2 + 7)

        cnt = Counter(ages)
        return sum(
            request(a, b) * cnt[a] * (cnt[b] - (a == b))
            for a in cnt
            for b in cnt)


print(Solution().numFriendRequests([16, 16]))
