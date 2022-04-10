"""
https://leetcode.com/problems/repeated-dna-sequences/
"""


from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 11:
            return []

        visited, rslt = set(), set()
        for i in range(n - 9):
            chkStr = s[i: i + 10]
            if chkStr not in visited:
                visited.add(chkStr)
            else:
                rslt.add(chkStr)

        return list(rslt)


s = 'A' * 12
print(Solution().findRepeatedDnaSequences(s))
