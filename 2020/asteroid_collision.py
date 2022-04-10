"""
https://leetcode.com/problems/asteroid-collision/
"""


from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        rslt = []
        for asteroid in asteroids:
            if asteroid < 0:
                while rslt and rslt[-1] > 0 and rslt[-1] < abs(asteroid):
                    rslt.pop()

                if rslt:
                    if rslt[-1] < 0:
                        rslt.append(asteroid)
                    elif rslt[-1] == abs(asteroid):
                        rslt.pop()
                else:
                    rslt.append(asteroid)
            else:
                rslt.append(asteroid)

        return rslt


print(Solution().asteroidCollision([-2, -1, 1, 2]))
