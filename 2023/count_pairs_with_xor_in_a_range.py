"""
https://leetcode.com/problems/count-pairs-with-xor-in-a-range/
"""


from collections import Counter


class Solution:
    def countPairs(self, A: list[int], low: int, high: int) -> int:
        def test(A, x):
            count = Counter(A)
            res = 0
            while x:
                if x & 1:
                    res += sum(count[a] * count[(x - 1) ^ a] for a in count)
                count = Counter(
                    {a >> 1: count[a] + count[a ^ 1] for a in count})
                x >>= 1
            return res // 2
        return test(A, high + 1) - test(A, low)
