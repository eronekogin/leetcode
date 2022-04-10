"""
https://leetcode.com/problems/check-array-formation-through-concatenation/
"""


from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        memo = {p[0]: p for p in pieces}
        i, N = 0, len(arr)
        while i < N:
            if arr[i] not in memo:
                return False

            p = memo[arr[i]]
            if arr[i: i + len(p)] != p:
                return False

            i += len(p)

        return True


print(Solution().canFormArray([91, 4, 64, 78], [[78], [4, 64], [91]]))
