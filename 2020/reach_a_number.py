"""
https://leetcode.com/problems/reach-a-number/
"""


class Solution:
    def reachNumber(self, target: int) -> int:
        """
        1. This problem could be taken as to put + or - sign between 1, 2, ...
            , k so that their sum equal to the target.
        2. When target < 0, it could be formed with the same steps as
            abs(target) as we could always change the signs accordingly. So we
            reduce the problem to only consider when target > 0.
        3. Then we could calculate the nearest k where 1 + ... + k >= target,
            which means (k + 1) * k >= target, which means
            k >= ((8t + 1) ** 0.5 - 1) / 2
        4. Then let's start with k = int(((8t + 1) ** 0.5 - 1) / 2), the sum
            is (k + 1) * k / 2, delta = sum - target
            4.1 If delta < 0, we keep increasing k.
            4.2 If delta > 0, check if delta is an even number. As if we change
                any sign in the middle of 1 + 2 + ... + k, suppose we change
                the sign at number x, then it will add 2x to the current delta.
                In this case, if our current delta is an even number, we could
                change the sign at num = delta / 2 to satisfy the sum.
                4.2.1 If delta is an odd number, keep increasing k and check
                    if the new delta is an even number.
        """
        t = abs(target)
        k = int(((8 * t + 1) ** 0.5 - 1) / 2)
        delta = ((k * (k + 1)) >> 1) - t
        while delta < 0 or delta & 1:
            k += 1
            delta += k

        return k


print(Solution().reachNumber(5))
