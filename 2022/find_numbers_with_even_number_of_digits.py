"""
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
"""


class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        def count_digits(num: int) -> int:
            currNum, cnt = num, 0
            while currNum:
                currNum = currNum // 10
                cnt += 1

            return cnt

        return sum(count_digits(num) & 1 == 0 for num in nums)
