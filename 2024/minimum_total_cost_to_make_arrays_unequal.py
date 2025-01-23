"""
https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def minimum_total_cost(self, nums1: list[int], nums2: list[int]) -> int:
        """
        minimum total cost
        """
        n = len(nums1)
        candidates = {i for i in range(n) if nums1[i] == nums2[i]}

        if not candidates:  # All different.
            return 0

        cnt = Counter(nums1[i] for i in candidates)
        major, freq = cnt.most_common(1)[0]
        remain_moves = max(freq * 2 - len(candidates), 0)

        for i in range(n):
            if remain_moves <= 0:
                break

            if nums1[i] != major != nums2[i] and i not in candidates:
                remain_moves -= 1
                candidates.add(i)

        if remain_moves:  # Still need more moves.
            return -1

        return sum(candidates)
