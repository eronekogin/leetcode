"""
https://leetcode.com/problems/count-largest-group/
"""


from collections import Counter


class Solution:
    def countLargestGroup(self, n: int) -> int:
        def count_digits_sum(x: int) -> int:
            currSum = 0
            while x:
                x, r = divmod(x, 10)
                currSum += r

            return currSum

        cnt = Counter(count_digits_sum(i) for i in range(1, n + 1))
        maxGroupSize = max(cnt.values())
        return sum(v == maxGroupSize for v in cnt.values())
