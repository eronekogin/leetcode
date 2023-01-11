"""
https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/
"""


from bisect import bisect_left, bisect_right


class Solution:
    def waysToSplit(self, nums: list[int]) -> int:
        """
        Compute prefix sums for nums and at each index i, we want to see if
        it satisfies pre[i] <= pre[j] - pre[i] <= pre[-1] - pre[j].
        """
        preSums = [0]
        for num in nums:
            preSums.append(preSums[-1] + num)

        rslt = 0
        for l in range(1, len(nums)):
            m = bisect_left(preSums, 2 * preSums[l])
            r = bisect_right(preSums, (preSums[-1] + preSums[l]) >> 1)
            rslt += max(0, min(len(nums), r) - max(l + 1, m))

        return rslt % (10 ** 9 + 7)


print(Solution().waysToSplit([1, 2, 2, 2, 5, 0]))
