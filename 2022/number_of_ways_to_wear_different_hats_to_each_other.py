"""
https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/
"""


from functools import lru_cache


class Solution:
    def numberWays(self, hats: list[list[int]]) -> int:
        @lru_cache(None)
        def dp(hat: int, usedMask: int) -> int:
            # All persons are assigned with a hat.
            if bin(usedMask).count('1') == TOTAL_PERSON:
                return 1

            # Not enough hat to assign.
            if hat == TOTAL_HAT:
                return 0

            # Total combinations without using the current hat.
            cnt = dp(hat + 1, usedMask)

            # Then count how many combinations when using the current hat.
            for person in hat2people[hat]:
                # If the current person is not assigned already.
                if usedMask & (1 << person) == 0:
                    cnt += dp(hat + 1, usedMask | (1 << person))

            return cnt

        TOTAL_PERSON = len(hats)
        hat2people: list[list[int]] = [[] for _ in range(41)]
        for person, preferredHats in enumerate(hats):
            for hat in preferredHats:
                hat2people[hat].append(person)

        # Filter out hats that no one want.
        hat2people = [h for h in hat2people if h]
        TOTAL_HAT = len(hat2people)

        # Not enough hats
        if TOTAL_HAT < TOTAL_PERSON:
            return 0

        return dp(0, 0) % (10 ** 9 + 7)
