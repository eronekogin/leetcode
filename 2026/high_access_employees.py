"""
https://leetcode.com/problems/high-access-employees/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def find_high_access_employees(self, access_times: list[list[str]]) -> list[str]:
        """
        Docstring for find_high_access_employees

        :param self: Description
        :param access_times: Description
        :type access_times: list[list[str]]
        :return: Description
        :rtype: list[str]
        """
        candidates: list[str] = []
        memo: dict[str, list[int]] = {}
        for name, t in access_times:
            if name not in memo:
                memo[name] = []

            memo[name].append(int(t[:2]) * 60 + int(t[2:]))

        for name, values in memo.items():
            if len(values) < 3:
                continue

            sv = sorted(values)
            if any(b - a < 60 for a, b in zip(sv, sv[2:])):
                candidates.append(name)

        return candidates
