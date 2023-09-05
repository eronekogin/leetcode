"""
https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/
"""


class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        """
        Suppose the radius of the square is r, then the total number of apple on the perimeter =
            4r + 8(r + 1) + ... + 8(2r - 1) + 4 * 2r
            = 4r + 8 * ((r + 1 + 2r - 1) * (2r - 1 - r - 1 + 1) // 2) + 4 * 2r
            = 4r + 12r^2 - 12 r + 8r
            = 12 * r * r
        """
        r = currentApples = 0
        while currentApples < neededApples:
            r += 1
            currentApples += 12 * r * r
        
        return r * 8
    

print(Solution().minimumPerimeter(1000000000))