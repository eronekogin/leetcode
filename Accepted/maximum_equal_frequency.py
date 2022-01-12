"""
https://leetcode.com/problems/maximum-equal-frequency/
"""


from collections import Counter


class Solution:
    def maxEqualFreq(self, nums: list[int]) -> int:
        """
        1. cnt stores the counter of each numbers.
        2. freqs stores the frequency of the counters.
        3. Then in order to satisfy the requirement, we have three cases:
            3.1 All elements occur once, which means maxFreq = 1
            3.2 All elements occur maxFreq times except one element occur once,
                which means maxFreq * freqs[maxFreq] + 1 == i + 1
            3.3 All elements occur maxFreq - 1 times, except one element occur
                maxFreq times, which means (maxFreq - 1) * freqs[maxFreq - 1] +
                maxFreq == i + 1.
        """
        cnt = Counter()
        freqs = Counter()
        maxFreq = 0
        rslt = 0
        for i, num in enumerate(nums):
            cnt[num] += 1
            freqs[cnt[num] - 1] -= 1
            freqs[cnt[num]] += 1
            maxFreq = max(maxFreq, cnt[num])
            if maxFreq * freqs[maxFreq] == i or (maxFreq - 1) * (freqs[maxFreq - 1] + 1) == i or maxFreq == 1:
                rslt = i + 1

        return rslt
