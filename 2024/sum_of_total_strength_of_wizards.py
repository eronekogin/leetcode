"""
https://leetcode.com/problems/sum-of-total-strength-of-wizards/description/
"""


from itertools import accumulate


class Solution:
    """
    Solution
    """

    def total_strength(self, strength: list[int]) -> int:
        """
        For a number at index i, suppose the first left
        smaller number is at index l and the first right
        smaller number is at index r, then we have the subarray
        as follows:
          al, a2, a3, ..., ai, b1, b2, ... , br

        Then for any subarray that includes ai, we have
        i - l choices of start position, and we have r - i choices
        of end position, and for such subarray, its total strengh
        is ai * (sum[end] - sum[start])

        Then consider the pairs of (start, end)

        for start, we have i - l choices, like (i - l) * (sum[b1] + sum[b2] + ... + sum[br]),
        for end , we have r - i choices, like (r - i) * (sum[al] + sum[a2] + ... + sum[ai]),
        """
        m = 10 ** 9 + 7
        n = len(strength)

        next_right_small = [n] * n
        stack = []
        for i, x in enumerate(strength):
            while stack and strength[stack[-1]] > x:
                next_right_small[stack.pop()] = i

            stack.append(i)

        prev_left_small = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] >= strength[i]:
                prev_left_small[stack.pop()] = i

            stack.append(i)

        rslt = 0
        prefix_sums = list(accumulate(accumulate(strength), initial=0))
        for i, x in enumerate(strength):
            l, r = prev_left_small[i], next_right_small[i]
            left = prefix_sums[i] - prefix_sums[max(l, 0)]
            right = prefix_sums[r] - prefix_sums[i]
            ln, rn = i - l, r - i
            rslt += x * (right * ln - left * rn)

        return rslt % m


print(Solution().total_strength([1, 3, 1, 2]))
