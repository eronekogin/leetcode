"""
https://leetcode.com/problems/decoded-string-at-index/
"""


class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        # Calculate the total size of S until it is greater than K.
        totalSize = 0
        end, n = -1, len(S)
        while end < n and totalSize < K:
            end += 1
            if S[end].isnumeric():
                totalSize *= int(S[end])
            else:
                totalSize += 1

        # Scan from end back to start to get the target char.
        target = K
        for i in range(end, -1, -1):
            if S[i].isnumeric():
                totalSize //= int(S[i])
                target %= totalSize
            else:
                if target == 0 or target == totalSize:
                    return S[i]

                totalSize -= 1


print(Solution().decodeAtIndex('leet2code3', 10))
