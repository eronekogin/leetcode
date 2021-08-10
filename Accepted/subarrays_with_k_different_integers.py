"""
https://leetcode.com/problems/subarrays-with-k-different-integers/
"""


from collections import Counter


class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        """
        The problem could be transferred to get the number of subarrays that
        have at most k unique numbers. then the number of subarrays that
        have exact k unique numbers = atMost(nums, k) - atMost(nums, k - 1).
        """
        def calcAtMost(k: int) -> int:
            """
            Use sliding window to calculate the number of subarrays that
            have at most k unique numbers.
            """
            cnt = Counter()
            rslt = start = 0
            for end in range(len(nums)):
                if cnt[nums[end]] == 0:  # Add a new unique number
                    k -= 1

                cnt[nums[end]] += 1
                while k < 0:
                    cnt[nums[start]] -= 1
                    if cnt[nums[start]] == 0:
                        k += 1

                    start += 1

                # Now we have end - start + 1 subarrays which ends at
                # the current end that have at most k unique numbers.
                rslt += end - start + 1

            return rslt

        return calcAtMost(k) - calcAtMost(k - 1)
