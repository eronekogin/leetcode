"""
https://leetcode.com/problems/count-items-matching-a-rule/
"""


class Solution:
    def countMatches(
        self,
        items: list[list[str]],
        ruleKey: str,
        ruleValue: str
    ) -> int:
        return sum(
            (ruleKey == 'type' and ruleValue == type) or
            (ruleKey == 'color' and ruleValue == color) or
            (ruleKey == 'name' and ruleValue == name)
            for type, color, name in items
        )
