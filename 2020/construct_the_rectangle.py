"""
https://leetcode.com/problems/construct-the-rectangle/
"""


from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        """
        L is always greater or equal to W, which means area = L*W >= W^2, so
        we have W <= area^0.5. Then we could scan from the largest w to see
        if there is an integer L matches it. 
        """
        w = int(area ** 0.5)
        while area % w:
            w -= 1

        return [area // w, w]


print(Solution().constructRectangle(10))
