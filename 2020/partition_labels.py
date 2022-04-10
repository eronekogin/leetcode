"""
https://leetcode.com/problems/partition-labels/
"""


from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        lastIndexes = {}  # {unique char in S: last index the char occurs.}
        for i, c in enumerate(S):
            lastIndexes[c] = i

        i, n, rslt = 0, len(S), []
        while i < n:
            end = lastIndexes[S[i]]
            newChars = set(S[i + 1: end])
            while newChars:
                start = end + 1
                end = max(end, max(lastIndexes[c] for c in newChars))
                newChars = set(S[start: end])

            rslt.append(end - i + 1)
            i = end + 1

        return rslt


print(Solution().partitionLabels2("qiejxqfnqceocmy"))
