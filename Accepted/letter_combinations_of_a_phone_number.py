"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""


class Solution:
    def letterCombinations(self, digits: 'str') -> 'List[str]':
        letterMap = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                     '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        rslt = []

        for num in digits:
            letters = letterMap.get(num)

            if letters is None:  # When input has invalid digit.
                rslt = []
                break

            if len(rslt) == 0:  # When first time.
                rslt = [c for c in letters]
            else:
                rslt = [subRslt + c for subRslt in rslt for c in letters]

        return rslt


print(Solution().letterCombinations('23'))
