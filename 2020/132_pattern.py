"""
https://leetcode.com/problems/132-pattern/
"""


from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
        1. Try to scan from the end of the input list.
        2. Keep collecting all the qualified thrid numbers into the stack:
            2.1 A qualified third number is a number that has a greater number
                comes before itself.
            2.2 The third variable holds the current maximum number from all the
                qualified ones.
        3. Once the current number is less than the current third, the current
            number becomes the first number, thus we have found a 132 pattern.
        4. If the current number is greater than the current third, it becomes
            a qualified second number.
            4.1 Then we simply update the current third with the maximum one
                from the third number stack which is less than the current
                second number.
        """
        thirds, third = [], float('-inf')
        for num in reversed(nums):
            if num < third:
                # The current number becomes a candidate for the first number.
                # Thus a 132 pattern is found.
                return True

            # Now the current number becomes a candidate for the second number.
            # Try to find the maximum third from thirds that is qualified for
            # the current second number.
            while thirds and thirds[-1] < num:
                third = thirds.pop()

            # Append the current number to the thirds as it is now becomes a
            # possible third number candidate for the next round.
            thirds.append(num)

        return False  # 132 pattern is not found.
