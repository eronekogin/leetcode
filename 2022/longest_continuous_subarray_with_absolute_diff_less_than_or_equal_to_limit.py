"""
https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
"""


from collections import deque


class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        maxQueue, minQueue = deque(), deque()
        start = 0
        for num in nums:
            # Keep the maximum number at front.
            while maxQueue and num > maxQueue[-1]:
                maxQueue.pop()

            # Keep the minimum number at front.
            while minQueue and num < minQueue[-1]:
                minQueue.pop()

            maxQueue.append(num)
            minQueue.append(num)

            if maxQueue[0] - minQueue[0] > limit:
                if maxQueue[0] == nums[start]:
                    maxQueue.popleft()

                if minQueue[0] == nums[start]:
                    minQueue.popleft()

                start += 1

        return len(nums) - start


print(Solution().longestSubarray([8, 2, 4, 7], 4))
