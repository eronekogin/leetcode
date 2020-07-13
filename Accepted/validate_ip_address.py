"""
https://leetcode.com/problems/validate-ip-address/
"""


class Solution:
    def validIPAddress(self, IP: str) -> str:
        hexChars = '0123456789ABCDEFabcdef'
        if '.' in IP:
            groups = IP.split('.')
            if len(groups) != 4:
                return 'Neither'

            for group in groups:
                if len(group) > 3 or (
                        len(group) > 1 and group[0] == '0') or\
                        not group.isdecimal() or int(group) > 255:
                    return 'Neither'

            return 'IPv4'
        elif ':' in IP:
            groups = IP.split(':')
            if len(groups) != 8:
                return 'Neither'

            for group in groups:
                if len(group) > 4 or len(group) < 1:
                    return 'Neither'

                for c in group:
                    if c not in hexChars:
                        return 'Neither'

            return 'IPv6'
        else:
            return 'Neither'
