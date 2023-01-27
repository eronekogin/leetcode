"""
https://leetcode.com/problems/minimum-number-of-people-to-teach/
"""


from collections import Counter


class Solution:
    def minimumTeachings(
        self,
        n: int,
        languages: list[list[int]],
        friendships: list[list[int]]
    ) -> int:
        speakLans = [set(l) for l in languages]
        strangers = set()
        for u, v in friendships:
            u -= 1
            v -= 1
            if speakLans[u] & speakLans[v]:  # Already be able to communicate.
                continue

            strangers.add(u)
            strangers.add(v)

        cnt = Counter()
        for stranger in strangers:
            for l in speakLans[stranger]:
                cnt[l] += 1

        if not strangers:
            return 0

        return len(strangers) - max(cnt.values())
