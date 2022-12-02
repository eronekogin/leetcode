"""
https://leetcode.com/problems/minimum-incompatibility/
"""


class Solution:
    def minimumIncompatibility(self, nums: list[int], k: int) -> int:
        def fn(i: int, cand: int):
            nonlocal minSum

            if cand + N - i - sum(not x for x in stack) > minSum:
                # Cannot get a smaller incompatible than the current minSum.
                return

            if i == N:
                minSum = cand
            else:
                currNum = sortedNums[i]
                for j in range(k):
                    if (
                        len(stack[j]) < subsetSize and
                        (not stack[j] or stack[j][-1] != currNum) and
                        (not j or stack[j - 1] != stack[j])
                    ):
                        stack[j].append(currNum)
                        if len(stack[j]) == 1:
                            fn(i + 1, cand)
                        else:
                            fn(i + 1, cand + stack[j][-1] - stack[j][-2])

                        stack[j].pop()

        N = len(nums)
        subsetSize = N // k
        sortedNums = sorted(nums)
        minSum = float('inf')
        stack = [[] for _ in range(k)]
        fn(0, 0)
        if minSum < float('inf'):
            return minSum

        return -1  # Impossible to distribute
