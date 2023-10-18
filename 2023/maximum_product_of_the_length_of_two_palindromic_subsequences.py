"""
https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/
"""


class Solution:
    """
    Solution.
    """

    def max_product(self, s: str) -> int:
        """
        max product
        """
        n = len(s)
        masks: list[tuple[int, int]] = []

        # Build palindrome masks.
        for mask in range(1, 1 << n):
            subseq: list[str] = []

            # Build actual sub sequence based on mask.
            for i in range(n):
                if mask & (1 << i) > 0:
                    subseq.append(s[i])

            if subseq == subseq[::-1]:
                masks.append((mask, len(subseq)))

        masks.sort(key=lambda x: x[1], reverse=True)
        rslt = 0

        # Check each pair of palindrome and make sure they are disjoint or not.
        n2 = len(masks)
        for i in range(n2 - 1):
            m1, l1 = masks[i]

            # Break early as the remaining ones cannot form a larger result.
            if l1 * l1 < rslt:
                break

            for j in range(i + 1, n2):
                m2, l2 = masks[j]

                if m1 & m2 == 0 and l1 * l2 > rslt:
                    rslt = l1 * l2
                    break  # Break early again.

        return rslt
