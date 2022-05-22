"""
https://leetcode.com/problems/html-entity-parser/
"""


class Solution:
    def entityParser(self, text: str) -> str:
        mapping = [
            ('&quot;', '"'),
            ('&apos;', "'"),
            ('&gt;', '>'),
            ('&lt;', '<'),
            ('&frasl;', '/'),
            ('&amp;', '&'),
        ]
        rslt = text
        for key, value in mapping:
            rslt = rslt.replace(key, value)

        return rslt
