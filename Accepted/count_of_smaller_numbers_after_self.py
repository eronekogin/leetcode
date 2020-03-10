"""
https://leetcode.com/problems/count-of-smaller-numbers-after-self/
"""


from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        Use the idea from merge sort.
        """
        N = len(nums)
        rslt = [0] * N

        def sort(idxs: List[int]):
            n = len(idxs)
            m = n >> 1
            if m:
                lp, rp = sort(idxs[:m]), sort(idxs[m:])

                # Scan from right to left of idxs to determine
                # how many small numbers to the right of the current number.
                for i in reversed(range(n)):
                    # If lp[-1] is greater than rp[-1], it means the last
                    # of lp is greater than all the numbers in rp,
                    # so add the length of the rp to the current counter
                    # of lp[-1].
                    if not rp or lp and nums[lp[-1]] > nums[rp[-1]]:
                        rslt[lp[-1]] += len(rp)  # Count number.
                        idxs[i] = lp.pop()  # Merge to the original list.
                    else:
                        idxs[i] = rp.pop()  # Just merge to the original list.

            return idxs

        sort(list(range(N)))
        return rslt


print(Solution().countSmaller([1, 9, 7, 8, 5]))
