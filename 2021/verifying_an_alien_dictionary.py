"""
https://leetcode.com/problems/verifying-an-alien-dictionary/
"""


class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        def less_or_equal(w1: str, w2: str) -> bool:
            if len(w1) > len(w2):
                return not less_or_equal(w2, w1)

            for c1, c2 in zip(w1, w2):
                if memo[c1] < memo[c2]:
                    return True
                elif memo[c1] > memo[c2]:
                    return False

            return True  # w1 and w2 are the same.

        memo = {c: i for i, c in enumerate(order)}
        return all(less_or_equal(w1, w2) for w1, w2 in zip(words, words[1:]))


print(Solution().isAlienSorted(["kuvp", "q"],
                               "ngxlkthsjuoqcpavbfdermiywz"))
