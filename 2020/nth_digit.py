"""
https://leetcode.com/problems/nth-digit/
"""


class Solution:
    def findNthDigit(self, n: int) -> int:
        """
        Suppose n = 2886.
        1. 1~9: currNum=2886,start=1,step=1,gap=9
        2. 10~99: currNum=2877,start=10,step=2,gap=90
        3. 100~999: currNum=2697,start=100,step=3,gap=900

        The total digits from 100 to 999 is 900*3=2700 > 2697, so the nth
        digit falls in the range 100 to 999.

        For the area 3, the starting index is 9 + 90 * 2 + 1 = 190.
        So the offset of the nth digit in area 3 is 2886 - 190 = 2696.

        divmod(2696, 3) = 898, 2, which means the actual number the nth
        digit falls is 100 + 898.

        So the overall index of the first 9 in 998 is 190 + 898 * 3 = 2884,
        then the 2886th digit will be the third number of 998 which is 8.
        """
        currNum, start, step, gap = n, 1, 1, 9
        while currNum > step * gap:
            currNum -= step * gap
            step += 1
            start *= 10
            gap *= 10

        q, r = divmod(currNum - 1, step)
        return int(str(start + q)[r])
