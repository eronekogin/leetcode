"""
https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/
"""


from collections import deque


class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        """
        1. Even flips equal to zero flip, while Odd flips equal to one flip.
        2. For minimum purpose, we should flip each time when we come across
            a zero.
        3. Then we use a queue to indicate whether the current position has
            been flipped or not:
            3.1 If nums[i] == 1 and index i has been flipped before, then it
                should become a zero now and we have to flip it again.
            3.2 If nums[i] == 0 and index i has not been flipped before, we
                have to flip it to make it 1.
            3.3 For other cases, we don't need to flip at the current index.
        4. When we need to flip at the current index but found that the
            remaining of the array is not long enough, we could never achieve
            the goal and should return -1.
        5. When our scanning index has passed the last flipped index, we
            should pop it from the queue.
        """
        currFlips = deque()
        totalFlips = 0
        N = len(nums)
        for i, num in enumerate(nums):
            if len(currFlips) & 1:  # Odd flips.
                isFlipped = 1
            else:  # Even flips
                isFlipped = 0

            if num == isFlipped:  # Need to flip at index i.
                if i + k > N:
                    return -1

                totalFlips += 1
                currFlips.append(i + k - 1)

            if currFlips and currFlips[0] <= i:
                currFlips.popleft()

        return totalFlips


print(Solution().minKBitFlips([0, 1, 0], 1))
