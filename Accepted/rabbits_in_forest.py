"""
https://leetcode.com/problems/rabbits-in-forest/
"""


class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        """
        1. If x + 1 rabbits have the same color, then we will have x + 1
            rabbits answer x.
        2. So each time we come across a new answer x, we suppose there are
            at least x + 1 rabbits and add it to our result.
        3. Then if we have n rabbits answer x:
            3.1 if n % (x + 1) == 0, we have at least n rabbits with 
                n // (x + 1) colors.
            3.2 If n % (x + 1) != 0, we have at least (n // (x + 1) + 1)
                colors, which means we should have at least
                (n // (x + 1) + 1) * (x + 1) rabbits.
        4. So for each new color, once it reaches i + 1, the remaining
            occurrence of the same color will be taken as a different color
            and we need to add the corresponding minimum rabbits to the result.
        """
        rslt, memo = 0, {}
        for cnt in answers:
            if memo.get(cnt, 0) % (cnt + 1) == 0:
                rslt += cnt + 1

            memo[cnt] = memo.get(cnt, 0) + 1

        return rslt
