"""
https://leetcode.com/problems/longest-mountain-in-array/
"""


from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        maxLen = start = 0
        n = len(A)
        while start < n:
            end = start
            if end + 1 < n and A[end + 1] > A[end]:
                while end + 1 < n and A[end + 1] > A[end]:  # Find peak first.
                    end += 1

                if end + 1 < n and A[end] > A[end + 1]:  # Having down part.
                    while end + 1 < n and A[end] > A[end + 1]:  # Find valley.
                        end += 1

                    maxLen = max(maxLen, end - start + 1)

                start = end
            else:
                start += 1

        return maxLen


print(Solution().longestMountain([2, 1, 4, 7, 3, 2, 5]))
