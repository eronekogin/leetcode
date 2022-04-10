"""
https://leetcode.com/problems/maximum-swap/
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        1. Store each number's last occurred position to the lastIndexes list.
        2. Scan the number from left to right. When the current digit has a
            larger digit in the remaining part, swap them.
        """
        s = list(str(num))
        lastIndexes = {c: i for i, c in enumerate(s)}
        for i, c in enumerate(s):
            for swap in range(9, int(c), -1):
                swapIdx = lastIndexes.get(str(swap), -1)
                if swapIdx > i:
                    s[i], s[swapIdx] = s[swapIdx], s[i]
                    return int(''.join(s))

        return num  # No need to swap.

    def maximumSwap2(self, num: int) -> int:
        """
        1. Scan num from right to left and store the largest index of the
            current maximum number.
        2. We also check the smallest index of the number that is less than the
            current maximum number, which will be our candidate to swap.
        """
        s = list(str(num))
        n = len(s) - 1
        swapMinIdx = swapMaxIdx = currMaxIdx = n
        for i in range(n, -1, -1):
            if s[i] > s[currMaxIdx]:
                currMaxIdx = i
            elif s[i] < s[currMaxIdx]:
                swapMinIdx, swapMaxIdx = i, currMaxIdx

        s[swapMinIdx], s[swapMaxIdx] = s[swapMaxIdx], s[swapMinIdx]
        return int(''.join(s))


print(Solution().maximumSwap(98368))
