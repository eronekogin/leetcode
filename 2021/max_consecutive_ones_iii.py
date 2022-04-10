"""
https://leetcode.com/problems/max-consecutive-ones-iii/
"""


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        """
        1. When coming across a zero, we need to flip it to make the current
            window larger.
        2. When the total flips exceed the maximum limit k, we shrink our
            current window by removing the leftmost item.
        3. Then slide the current window on the list until we find a longer
            window.
        4. When the window reaching the end, it is our longest window.
        """
        start = 0
        flipped = k
        for num in nums:
            flipped -= 1 - num
            if flipped < 0:
                flipped += 1 - nums[start]
                start += 1

        return len(nums) - start


print(Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
