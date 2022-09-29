"""
https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/
"""


class Solution:
    def maxSumRangeQuery(
        self,
        nums: list[int],
        requests: list[list[int]]
    ) -> int:
        """
        Sweep line method:
            Suppose we have interval [1, 3], [3, 5], initially we have
            cnt = [0, 0, 0, 0, 0, 0, 0, 0], n = 5, then:
                after [1, 3], cnt = [0, 1, 0, 0, -1, 0, 0, 0]
                after [3, 5], cnt = [0, 1, 0, 1, -1, 0, -1, 0]

            Then the prefix sum of cnt will be:
                cnt = [0, 1, 1, 2, 1, 1, 0, 0]

            We will see that index 1 and 2 are counted once, index 3 are
            counted twice, and index 4 and 5 are counted once.
        """
        N = len(nums)
        cnt = [0] * (N + 1)

        # Mark the start and end position for each interval in cnt.
        for start, end in requests:
            cnt[start] += 1
            cnt[end + 1] -= 1

        # Then count the frequency of each index based on the prefix sum in
        # cnt.
        for i in range(1, N + 1):
            cnt[i] += cnt[i - 1]

        # Then for the index having more frequency, it should be placed with
        # larger value.
        total = 0
        for f, v in zip(sorted(cnt[:N]), sorted(nums)):
            total += f * v

        return total % (10 ** 9 + 7)
