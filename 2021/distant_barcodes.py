"""
https://leetcode.com/problems/distant-barcodes/
"""


from collections import Counter


class Solution:
    def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
        """
        Try to put the barcodes with most occurrences separately, which is
        to put them to places like i, i + 2, i + 4, ...
        Then repeat the above process until all the codes are settled.
        """
        if len(barcodes) < 3:
            return barcodes

        i, N = 0, len(barcodes)
        rslt = [0] * N

        for code, freq in Counter(barcodes).most_common():
            for _ in range(freq):
                rslt[i] = code
                i += 2

                # If reaching the end, back to front to fill the remain entries.
                if i >= N:
                    i = 1

        return rslt


print(Solution().rearrangeBarcodes([2, 2, 2, 1, 5]))
