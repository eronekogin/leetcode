"""
https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/description/
"""


from heapq import heapify, heappop, heappush


class Solution:
    """
    Solution
    """
    def get_final_state(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        """
        get final state
        """
        if multiplier == 1:
            return nums

        n = len(nums)
        unseen = set(range(n))


        # Go through the loop until all numbers in nums have been multipled by
        # the multiplier once.
        heap = [(x, i) for i, x in enumerate(nums)]
        heapify(heap)
        remain = k
        while remain and unseen:
            x, i = heappop(heap)
            heappush(heap, (x * multiplier, i))
            remain -= 1
            unseen.discard(i)


        # Then we can simply calculate the module power of multipler
        mod = 10 ** 9 + 7
        rslt = [0] * n
        q, r = divmod(remain, n)

        for i in range(n):
            x, j = heappop(heap)
            rslt[j] = (x * pow(multiplier, q + (i < r), mod)) % mod

        return rslt
