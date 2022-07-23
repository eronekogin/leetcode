"""
https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/
"""


from collections import Counter


class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        nonZeroRemains = [num % k for num in arr if num % k != 0]
        if len(nonZeroRemains) & 1:
            # total number of zero remainins must be even in order to make
            # pairs by themselves.
            return False

        cnt = Counter(nonZeroRemains)
        for i in range(1, k):
            if i in cnt and cnt[i] != cnt[k - i]:
                return False

        return True


print(Solution().canArrange([3, 8, 17, 2, 5, 6],
                            10))
