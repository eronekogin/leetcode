"""
https://leetcode.com/problems/longest-increasing-subsequence/

See https://algorithmsandme.com/longest-increasing-subsequence-in-onlogn/ 
for more details.
"""


from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        lis = [nums[0]]

        def get_smallest_larger(t: int) -> int:
            """
            Get the smallest number in lis which is greater than t.
            """
            l, r = 0, len(lis) - 1
            while l < r:
                m = l + ((r - l) >> 1)  # (l + r) // 2.
                if lis[m] < t:
                    l = m + 1
                else:
                    r = m

            return l

        for num in nums:
            if num < lis[0]:
                # The current number is smaller than all numbers in lis.
                lis[0] = num
            elif num > lis[-1]:
                # The current number is greater than all numbers in lis.
                lis.append(num)
            else:
                # The current number is among the numbers in lis. Try to find
                # the smallest number in lis that is greater than the current
                # number, than replace it with the current number.
                lis[get_smallest_larger(num)] = num

        return len(lis)


print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
