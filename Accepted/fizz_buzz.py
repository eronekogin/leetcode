"""
https://leetcode.com/problems/fizz-buzz/
"""


from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        rslt = []
        for i in range(1, n + 1):
            if not i % 15:
                rslt.append('FizzBuzz')
            elif not i % 3:
                rslt.append('Fizz')
            elif not i % 5:
                rslt.append('Buzz')
            else:
                rslt.append(str(i))

        return rslt
