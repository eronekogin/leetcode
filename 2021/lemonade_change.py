"""
https://leetcode.com/problems/lemonade-change/
"""


class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        cnt5 = cnt10 = 0
        for bill in bills:
            if bill == 5:
                cnt5 += 1
            elif bill == 10:
                if not cnt5:
                    return False

                cnt5 -= 1
                cnt10 += 1
            else:  # bill == 20
                if cnt10 and cnt5:
                    cnt10 -= 1
                    cnt5 -= 1
                elif cnt5 >= 3:
                    cnt5 -= 3
                else:
                    return False

        return True
