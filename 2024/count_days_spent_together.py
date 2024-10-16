"""
https://leetcode.com/problems/count-days-spent-together/description/
"""


class Solution:
    """
    Solution
    """

    def count_days_together(
        self,
        arrive_alice: str,
        leave_alice: str,
        arrive_bob: str,
        leave_bob: str
    ) -> int:
        """
        count days together
        """
        def get_day(s: str):
            m, d = s.split('-')
            return sum(days[: int(m) - 1]) + int(d)

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        sa, ea = get_day(arrive_alice), get_day(leave_alice)
        sb, eb = get_day(arrive_bob), get_day(leave_bob)

        if ea < sb or sa > eb:
            return 0

        return min(ea, eb) - max(sa, sb) + 1


print(Solution().count_days_together("10-01", "10-31", "11-01", "12-31"))
