"""
https://leetcode.com/problems/bulb-switcher/
"""


class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        All the bulbs at first are turned on. So a bulb will stay on only 
        when it is toggled odd times during n rounds. The ith bulb will only
        be toggled at the pth round, while p is i's factor. Since i could be
        divided by itself, if i has a integer square root, it will have odd
        total factors except 1, otherwise it will have even total factors
        except 1. So this problem is to find out how many perfect square
        numbers that are less than n.
        """
        return int(n ** 0.5)


print(Solution().bulbSwitch(3))
