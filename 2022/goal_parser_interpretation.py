"""
https://leetcode.com/problems/goal-parser-interpretation/
"""


class Solution:
    def interpret(self, command: str) -> str:
        rslt = command.replace('()', 'o')
        return rslt.replace('(al)', 'al')
