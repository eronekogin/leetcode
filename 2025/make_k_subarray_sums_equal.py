"""
https://leetcode.com/problems/make-k-subarray-sums-equal/description/
"""


from math import gcd


class Solution:
    """
    Solution
    """

    def make_sub_k_sum_equal(self, arr: list[int], k: int) -> int:
        """
        Since we need to make sub array with length k equal, which means
        * if the array is not circular, every kth element should be the same
            after the operations, which means a[0] = a[k]
        * if the array is circular, we need every gcd(n, k) th element be
            the same after the operations.
        """
        n = len(arr)
        g = gcd(n, k)
        cnt = 0

        for i in range(g):
            tmp = sorted(arr[i::g])
            m = tmp[len(tmp) >> 1]
            cnt += sum(abs(x - m) for x in tmp)

        return cnt


print(Solution().make_sub_k_sum_equal([1, 4, 1, 3], 2))
