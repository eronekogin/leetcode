"""
https://leetcode.com/problems/sliding-window-maximum/
"""


from typing import List
from collections import deque


class Monoqueue:
    def __init__(self):
        """
        The main storage of the monotonic queue:
            The first item stands for the actual value.
            The second item stands for how many elements were deleted
                between this number and the one before it.
        """
        self.queue = deque()

    def push(self, val: int):
        cnt = 0
        while self.queue and self.queue[-1][0] < val:
            cnt += self.queue.pop()[1] + 1

        self.queue.append([val, cnt])

    def get_max(self) -> int:
        # The first element always hold the max number.
        return self.queue[0][0]

    def pop(self):
        if self.queue[0][1] > 0:  # Counter > 0.
            self.queue[0][1] -= 1
            return

        self.queue.popleft()


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or not k:  # Empty list or empty window.
            return []

        rslt, mq, n = [], Monoqueue(), len(nums)
        for i in range(k - 1):  # Push the first k - 1 numbers.
            mq.push(nums[i])

        for i in range(k - 1, n):  # Check the remaining.
            mq.push(nums[i])  # Add the kth number.
            rslt.append(mq.get_max())  # Store the current max.
            mq.pop()  # Get rid of the 1st number.

        return rslt

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        """
        Simplify the above solution by only storing the index of the maximum
        numbers from left to right.
        """
        rslt, queue, start = [], deque(), k - 1
        for i, num in enumerate(nums):
            while queue and nums[queue[-1]] < num:
                queue.pop()  # Remove indexes of the smaller number.

            queue.append(i)  # Append the current index.
            if queue[0] + k == i:  # The first index is out of window.
                queue.popleft()

            if i >= start:
                # The first index in the queue is the largest number.
                rslt.append(nums[queue[0]])

        return rslt


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(Solution().maxSlidingWindow(nums, k))
