"""
https://leetcode.com/problems/odd-even-jump/
"""


class Solution:
    def oddEvenJumps(self, arr: list[int]) -> int:
        N = len(arr)
        nextHighers, nextLowers = [0] * N, [0] * N
        stack = []
        for _, i in sorted([a, i] for i, a in enumerate(arr)):
            while stack and stack[-1] < i:
                nextHighers[stack.pop()] = i

            stack.append(i)

        stack = []
        for _, i in sorted([-a, i] for i, a in enumerate(arr)):
            while stack and stack[-1] < i:
                nextLowers[stack.pop()] = i

            stack.append(i)

        highers, lowers = [0] * N, [0] * N
        highers[-1] = lowers[-1] = 1
        for i in reversed(range(N - 1)):
            highers[i] = lowers[nextHighers[i]]
            lowers[i] = highers[nextLowers[i]]

        return sum(highers)
