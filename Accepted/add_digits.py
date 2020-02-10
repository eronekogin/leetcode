"""
https://leetcode.com/problems/add-digits/


See https://leetcode.com/problems/add-digits/discuss/68580/Accepted-C%2B%2B-O(1)-time-O(1)-space-1-Line-Solution-with-Detail-Explanations

for more details.
"""


class Solution:
    def addDigits(self, num: int) -> int:
        if not num:
            return 0

        return 1 + (num - 1) % 9
