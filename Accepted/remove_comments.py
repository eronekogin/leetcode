"""
https://leetcode.com/problems/remove-comments/
"""


from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        rslt, inBlock = [], False
        for line in source:
            i = 0
            if not inBlock:
                newLine = []

            while i < len(line):
                if line[i: i + 2] == '/*' and not inBlock:
                    inBlock = True
                    i += 1
                elif line[i: i + 2] == '*/' and inBlock:
                    inBlock = False
                    i += 1
                elif not inBlock and line[i: i + 2] == '//':
                    break
                elif not inBlock:
                    newLine.append(line[i])

                i += 1

            if newLine and not inBlock:
                rslt.append(''.join(newLine))

        return rslt


print(Solution().removeComments(
    [
        "/*Test program */",
        "int main()",
        "{ ",
        "  // variable declaration ",
        "int a, b, c;",
        "/* This is a test",
        "   multiline  ",
        "   comment for ",
        "   testing */",
        "a = b + c;", "}"]))
