"""
https://leetcode.com/problems/restore-ip-addresses/
"""

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # Presumption: s only contains digit chars.
        n, rslt, chkRange = len(s), [], [1, 2, 3]
        for w1 in chkRange:
            for w2 in chkRange:
                for w3 in chkRange:
                    w4 = n - w1 - w2 - w3
                    if 1 <= w4 <= 3:  # Possible ip found.
                        s1, s2, s3, s4 = (
                            s[:w1], s[w1: w1 + w2],
                            s[w1 + w2: w1 + w2 + w3], s[w1 + w2 + w3:])
                        if self.validate_ip(s1) and self.validate_ip(
                            s2) and self.validate_ip(s3) and self.validate_ip(
                                s4):
                            rslt.append('.'.join([s1, s2, s3, s4]))

        return rslt

    def validate_ip(self, s: str) -> bool:
        if len(s) == 1:
            return True

        if s.startswith('0'):
            return False  # Should not have leading zero when length > 1.

        if len(s) == 3 and s > '255':
            return False

        return True


print(Solution().restoreIpAddresses("25525511135"))
