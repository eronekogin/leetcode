"""
https://leetcode.com/problems/constrained-subsequence-sum/
"""


from collections import deque


class Solution:
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
        """
        Suppose maxSums[i] stands for the maximum result we could get when
        the subsequence is ended at nums[i]. Then we keep a decreasing deque
        to store the index of the pre calculated maximum result we could get
        so far. Then for each i, we try to combine it with the current
        maximum sum to see if we could achieve a greater sum. Then put the
        current index to the queue if greater sum is found.
        """
        N = len(nums)
        maxSums = list(nums)
        queue = deque()

        for i in range(N):
            if queue:
                maxSums[i] += maxSums[queue[0]]

            # The distance between the first element in queue and the current
            # index is greater than k.
            if queue and queue[0] <= i - k:
                queue.popleft()

            # Keep queue decreasing.
            while queue and maxSums[queue[-1]] <= maxSums[i]:
                queue.pop()

            # Add to queue if getting a positive max sum at index i.
            if maxSums[i] > 0:
                queue.append(i)

        return max(maxSums)
