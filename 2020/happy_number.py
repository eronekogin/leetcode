"""
https://leetcode.com/problems/happy-number/
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Similar as the algorithm we used to detect cycle in
        cycled list, here we move one step further by calculating
        the summary of the squares of the digits in the current number.
        """
        slow = fast = n
        while True:
            slow = self.get_square_sum(slow)
            fast = self.get_square_sum(self.get_square_sum(fast))
            if fast == 1:
                return True

            if slow == fast:
                return False

    def get_square_sum(self, n: int) -> int:
        currNum, rslt = n, 0
        while currNum:
            currNum, currDigit = divmod(currNum, 10)
            rslt += currDigit ** 2

        return rslt


print(Solution().isHappy(2))
