"""
https://leetcode.com/problems/count-subarrays-with-score-less-than-k/description/
"""


class Solution:
    """
    Solution
    """

    def count_subarrays(self, nums: list[int], k: int) -> int:
        """
        For a given index range i to j, suppose curr_sum stands for
        the sum of numbers from i to j, if curr_sum * (j - i + 1) < k,
        then all the subarrys inside this range will be the candidate,
        which is j - i + 1 subarrays
        """
        curr_sum = 0
        start = 0
        cnt = 0
        for end, x in enumerate(nums):
            curr_sum += x
            while curr_sum * (end - start + 1) >= k:
                curr_sum -= nums[start]
                start += 1

            cnt += end - start + 1

        return cnt


print(Solution().count_subarrays([1, 2, 9, 1, 5], 96))
