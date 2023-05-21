"""
https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/
"""


class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def next_perm(digits: list[str]):
            i = N - 1
            while i > 0 and digits[i - 1] >= digits[i]:
                i -= 1

            j = i
            while j < N and digits[i - 1] < digits[j]:
                j += 1

            digits[i - 1], digits[j - 1] = digits[j - 1], digits[i - 1]
            digits[i:] = digits[i:][::-1]
            return digits

        N = len(num)

        # Get the next kth smallest wonderful number.
        digits = list(num)
        for _ in range(k):
            digits = next_perm(digits)

        swaps = 0
        currDigits = list(num)
        for i in range(N):
            j = i
            while j < N and digits[i] != currDigits[j]:
                j += 1

            swaps += j - i
            currDigits[i: j + 1] = [currDigits[j]] + currDigits[i: j]

        return swaps
