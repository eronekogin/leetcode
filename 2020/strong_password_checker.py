"""
https://leetcode.com/problems/strong-password-checker/
"""


class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        noLower = noUpper = noDigit = 1
        changes = delOne = delTwo = 0
        for c in s:
            if noLower and c.islower():
                noLower = 0
            elif noUpper and c.isupper():
                noUpper = 0
            elif noDigit and c.isdecimal():
                noDigit = 0

            if not (noLower or noUpper or noDigit):
                break

        i, n = 2, len(s)
        while i < n:
            if s[i] == s[i - 1] == s[i - 2]:
                repeatLen = 2
                while i < n and s[i] == s[i - 1]:
                    repeatLen += 1
                    i += 1

                replaces, remain = divmod(repeatLen, 3)
                changes += replaces
                if remain == 0:
                    # When the length of the repeat chars is 3k,
                    # we need to make k replacements to obey the rule.
                    # But if we delete one char from the repeat chars,
                    # then we just need to make k - 1 replacements.
                    delOne += 1
                elif remain == 1:
                    # When the length of the repeat chars is 3k + 1,
                    # then we could delete two chars to make k - 1
                    # replacements.
                    delTwo += 1
            else:
                i += 1

        missing = noLower + noUpper + noDigit
        if n < 6:
            return max(missing, 6 - n)
        elif n <= 20:
            return max(missing, changes)
        else:
            dels = n - 20

            # Delete one char to reduce replacements.
            changes -= min(dels, delOne)

            # Delete two chars to reduce replacements.
            changes -= min(max(dels - delOne, 0), 2 * delTwo) // 2

            # For the current repeating sequences, they form as 3k + 2.
            # So we need to delete 3 chars to make k -1 replacements.
            changes -= max(dels - delOne - 2 * delTwo, 0) // 3

            return dels + max(missing, changes)


print(Solution().strongPasswordChecker("ABABABABABABABABABAB1"))
