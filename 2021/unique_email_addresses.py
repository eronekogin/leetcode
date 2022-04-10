"""
https://leetcode.com/problems/unique-email-addresses/
"""


class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        def parse_email(email: str) -> tuple[str]:
            localName, domainName = email.split('@')
            localName = localName.split('+')[0]  # Ignore '+'
            localName = ''.join(localName.split('.'))  # Combine '.'
            return (localName, domainName)

        return len({parse_email(email) for email in emails})
