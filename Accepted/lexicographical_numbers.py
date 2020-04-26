"""
https://leetcode.com/problems/lexicographical-numbers/
"""


from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        rslt = [1]
        while len(rslt) < n:
            nextNum = rslt[-1] * 10
            while nextNum > n:
                nextNum //= 10
                nextNum += 1
                while not nextNum % 10:
                    # Handle case when 199 + 1 = 200, where we need
                    # to restart couting from 2.
                    nextNum //= 10

            rslt.append(nextNum)

        return rslt


print(Solution().lexicalOrder(111))
