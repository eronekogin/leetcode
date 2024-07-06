"""
https://leetcode.com/problems/strong-password-checker-ii/description/
"""


class Solution:
    """
    Solution
    """

    def strong_password_checker_ii(self, password: str) -> bool:
        """
        strong password checker ii
        """

        if len(password) < 8:
            return False

        lower_cnt = upper_cnt = digit_cnt = special_cnt = 0
        for i, c in enumerate(password):
            lower_cnt += c.islower()
            upper_cnt += c.isupper()
            digit_cnt += c.isdigit()
            special_cnt += c in '!@#$%^&*()-+'

            if i > 0 and password[i] == password[i - 1]:
                return False

        return (
            lower_cnt > 0 and
            upper_cnt > 0 and
            digit_cnt > 0 and
            special_cnt > 0
        )
