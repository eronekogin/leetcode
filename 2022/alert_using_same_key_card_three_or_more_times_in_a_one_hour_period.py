"""
https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/
"""


from collections import deque, defaultdict


class Solution:
    def alertNames(self, keyName: list[str], keyTime: list[str]) -> list[str]:
        memo: defaultdict[str, list[int]] = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            hour, minute = map(int, time.split(':'))
            memo[name].append(hour * 60 + minute)

        alertNames: list[str] = []
        for name, times in memo.items():
            q: deque[int] = deque()
            for t in sorted(times):
                q.append(t)
                if q[-1] - q[0] > 60:
                    q.popleft()

                if len(q) >= 3:
                    alertNames.append(name)
                    break

        return sorted(alertNames)


print(Solution().alertNames(["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"],
                            ["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"]))
