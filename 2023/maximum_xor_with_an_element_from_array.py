"""
https://leetcode.com/problems/maximum-xor-with-an-element-from-array/
"""


from bisect import bisect_left, bisect_right


class Solution:
    def maximizeXor(
        self,
        nums: list[int],
        queries: list[list[int]]
    ) -> list[int]:
        sortedNums = sorted(nums)
        rslt: list[int] = []
        for x, m in queries:
            if m < sortedNums[0]:
                rslt.append(-1)
                continue

            start, end = 0, bisect_right(sortedNums, m)
            currNum = 0
            # Search from the most significant digit in m.
            bit = 1 << m.bit_length()
            while bit:
                nextNum = currNum + bit
                if sortedNums[start] >= nextNum:
                    # All numbers after start have this bit set already.
                    currNum = nextNum
                elif sortedNums[end - 1] >= nextNum:
                    # Some numbers before end could have this bit not set.
                    # So we use binary search to find the cut position.
                    cut = bisect_left(sortedNums, nextNum, start, end)
                    if x & bit:  # The current bit is set in x.
                        end = cut  # We want a different bit than what's in x.
                    else:
                        # Otherwise we take all the numbers after cut position.
                        start = cut
                        currNum = nextNum

                bit >>= 1

            rslt.append(currNum ^ x)

        return rslt
