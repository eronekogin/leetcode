"""
https://leetcode.com/problems/get-equal-substrings-within-budget/
"""


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        currCost = 0
        currLen = maxLen = 0
        start = 0
        for end in range(len(s)):
            currCost += abs(ord(s[end]) - ord(t[end]))
            currLen += 1
            if currCost > maxCost:
                maxLen = max(maxLen, currLen - 1)
                while currCost > maxCost:
                    currCost -= abs(ord(s[start]) - ord(t[start]))
                    start += 1
                    currLen -= 1

        return max(maxLen, currLen)

    def equalSubstring2(self, s: str, t: str, maxCost: int) -> int:
        """
        Doing it reversely. The reason that we don't need to keep checking
        the maximum length is because the sliding window will never be smaller
        than before: when we move the left bound with 1 position, we will also
        move the right bound.
        """
        currCost = maxCost
        start = 0
        for end in range(len(s)):
            currCost -= abs(ord(s[end]) - ord(t[end]))
            if currCost < 0:
                currCost += abs(ord(s[start]) - ord(t[start]))
                start += 1

        return end - start + 1


print(Solution().equalSubstring("krpgjbjjznpzdfy",
                                "nxargkbydxmsgby",
                                14))
