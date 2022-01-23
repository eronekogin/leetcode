"""
https://leetcode.com/problems/count-number-of-nice-subarrays/
"""


class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        def at_most(k: int) -> int:
            """
            Count how many subarrays contains at most k odd numbers.
            """
            rslt = 0
            start = 0
            requiredOddNumbers = k
            for end in range(len(nums)):
                requiredOddNumbers -= nums[end] & 1
                while requiredOddNumbers < 0:  # Not enough odd numbers.
                    requiredOddNumbers += nums[start] & 1
                    start += 1

                rslt += end - start + 1

            return rslt

        return at_most(k) - at_most(k - 1)
