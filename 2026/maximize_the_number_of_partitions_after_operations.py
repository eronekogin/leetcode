"""
https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/description/
"""


class Solution:
    """
    Solution
    """

    def max_partitions_after_operations(self, s: str, k: int) -> int:
        """
        max partitions after operations
        """
        offset = ord('a')
        n = len(s)

        # 0: represents the number of splits
        # 1: represents the mask of chars
        # 2: represents the number of distinct chars
        left = [[0] * 3 for _ in range(n)]
        right = [[0] * 3 for _ in range(n)]

        # Calculate left
        p, mask, cnt = 0, 0, 0
        for i in range(n - 1):
            curr = 1 << (ord(s[i]) - offset)

            if not mask & curr:
                cnt += 1
                if cnt <= k:
                    mask |= curr
                else:
                    p += 1
                    mask = curr
                    cnt = 1

            left[i + 1][0] = p
            left[i + 1][1] = mask
            left[i + 1][2] = cnt

        # Calculate right
        p, mask, cnt = 0, 0, 0
        for i in range(n - 1, 0, -1):
            curr = 1 << (ord(s[i]) - offset)

            if not mask & curr:
                cnt += 1
                if cnt <= k:
                    mask |= curr
                else:
                    p += 1
                    mask = curr
                    cnt = 1

            right[i - 1][0] = p
            right[i - 1][1] = mask
            right[i - 1][2] = cnt

        max_p = 0
        for i in range(n):
            p = left[i][0] + right[i][0] + 2
            mask = left[i][1] | right[i][1]
            d = bin(mask).count('1')

            if left[i][2] == k and right[i][2] == k and d < 26:
                p += 1
            elif min(d + 1, 26) <= k:
                p -= 1

            max_p = max(max_p, p)

        return max_p
