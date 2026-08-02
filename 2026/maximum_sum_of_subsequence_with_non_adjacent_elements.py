"""
https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_sum_sub_sequence(self, nums: list[int], queries: list[list[int]]) -> int:
        """
        maximum sum sub sequence
        """
        def build(tidx: int, lo: int, hi: int):
            if lo == hi:
                # When coming to the leaf node, its value comes from nums[lo]
                tree[tidx][0] = max(0, nums[lo])
            else:
                mid = (lo + hi) // 2

                build(2 * tidx + 1, lo, mid)
                build(2 * tidx + 2, mid + 1, hi)

                l0h0_1, l1h0_1, l0h1_1, l1h1_1 = tree[2 * tidx + 1]
                l0h0_2, l1h0_2, l0h1_2, l1h1_2 = tree[2 * tidx + 2]

                # lo to hi
                tree[tidx][0] = max(
                    l0h1_1 + l1h0_2,  # Exclude both mid and mid + 1
                    l0h0_1 + l1h0_2,  # Include mid, exclude mid + 1
                    l0h1_1 + l0h0_2  # Exclude mid, include mid + 1
                )

                # lo + 1 to hi
                tree[tidx][1] = max(
                    l1h1_1 + l1h0_2,
                    l1h0_1 + l1h0_2,
                    l1h1_1 + l0h0_2
                )

                # lo to hi - 1
                tree[tidx][2] = max(
                    l0h1_1 + l1h1_2,
                    l0h0_1 + l1h1_2,
                    l0h1_1 + l0h1_2
                )

                # lo + 1 to hi - 1
                tree[tidx][3] = max(
                    l1h1_1 + l1h1_2,
                    l1h0_1 + l1h1_2,
                    l1h1_1 + l0h1_2
                )

        def update(tidx: int, lo: int, hi: int, i: int, val: int):
            if lo == hi:
                # When coming to the leaf node, its value is max(0, input value)
                tree[tidx][0] = max(0, val)
            else:
                mid = (lo + hi) // 2

                if i > mid:
                    update(tidx * 2 + 2, mid + 1, hi, i, val)
                else:
                    update(tidx * 2 + 1, lo, mid, i, val)

                l0h0_1, l1h0_1, l0h1_1, l1h1_1 = tree[2 * tidx + 1]
                l0h0_2, l1h0_2, l0h1_2, l1h1_2 = tree[2 * tidx + 2]

                # lo to hi
                tree[tidx][0] = max(
                    l0h1_1 + l1h0_2, l0h0_1 + l1h0_2, l0h1_1 + l0h0_2)

                # lo + 1 to hi
                tree[tidx][1] = max(
                    l1h1_1 + l1h0_2, l1h0_1 + l1h0_2, l1h1_1 + l0h0_2)

                # lo to hi - 1
                tree[tidx][2] = max(
                    l0h1_1 + l1h1_2, l0h0_1 + l1h1_2, l0h1_1 + l0h1_2)

                # lo + 1 to hi - 1
                tree[tidx][3] = max(
                    l1h1_1 + l1h1_2, l1h0_1 + l1h1_2, l1h1_1 + l0h1_2)

        n = len(nums)
        tree = [[0] * 4 for _ in range(4 * n)]
        build(0, 0, n - 1)
        ans = 0
        for i, x in queries:
            update(0, 0, n - 1, i, x)
            ans += max(tree[0])

        return ans % 1_000_000_007
