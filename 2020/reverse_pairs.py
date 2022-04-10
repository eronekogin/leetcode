"""
https://leetcode.com/problems/reverse-pairs/
"""


from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """
        Use merge sort on the input list, and during each round of the merge
        sort, we count the number of important reverse pairs.
        """
        def count(start: int, end: int) -> int:
            if start >= end:  # No more items to be divided.
                return 0

            m = start + ((end - start) >> 1)
            pairCnt = count(start, m) + count(m + 1, end)

            # Now the left and right part are sorted, we need to calculate
            # the import reverse pairs across both sides.
            r = m + 1
            for l in range(start, m + 1):
                while r <= end and nums[l] > (nums[r] << 1):
                    r += 1

                pairCnt += r - (m + 1)

            # After count, sort and merge the result back to nums.
            nums[start: end + 1] = sorted(nums[start: end + 1])

            return pairCnt

        return count(0, len(nums) - 1)


print(Solution().reversePairs([1, 3, 2, 3, 1]))
