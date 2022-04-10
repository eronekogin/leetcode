"""
https://leetcode.com/problems/masking-personal-information/
"""


class Solution:
    def maskPII(self, S: str) -> str:
        def parse_email(w: str) -> str:
            first, remain = w.split('@')
            return '{0}*****{1}@{2}'.format(
                first[0], first[-1], remain).lower()

        def parse_phone(w: str) -> str:
            digits = [c for c in w if c.isdigit()]
            if len(digits) > 10:
                return '+{0}-***-***-{1}'.format(
                    '*' * (len(digits) - 10), ''.join(digits[-4:]))
            else:
                return '***-***-{0}'.format(''.join(digits[-4:]))

        if '@' in S:
            return parse_email(S)
        else:
            return parse_phone(S)
