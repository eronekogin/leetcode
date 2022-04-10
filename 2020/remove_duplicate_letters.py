"""
https://leetcode.com/problems/remove-duplicate-letters/
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Count how many times each char in s occurs.
        cnts = {}
        for c in s:
            cnts[c] = cnts.get(c, 0) + 1

        # Scan for smallest unique sub string in lexicographical order.
        rslt = []
        for c in s:
            cnts[c] -= 1  # Reduce total counter.
            if c not in rslt:  # Come across a new char.
                # Scan the current result to remove all the chars
                # that are greater than the current char while also occurs
                # after the current char.
                while rslt and rslt[-1] > c and cnts[rslt[-1]]:
                    rslt.pop()

                rslt.append(c)

        return ''.join(rslt)


print(Solution().removeDuplicateLetters('bcabc'))
