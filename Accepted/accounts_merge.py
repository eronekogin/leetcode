"""
https://leetcode.com/problems/accounts-merge/
"""


from typing import List

from collections import defaultdict


class DSU:

    def __init__(self, size: int):
        self._parents = list(range(size + 1))

    def find_ancestor(self, x: int) -> int:
        """
        For all ancestors, its parent equals to itself.
        """
        if self._parents[x] != x:
            self._parents[x] = self.find_ancestor(self._parents[x])

        return self._parents[x]

    def union(self, x: int, y: int) -> None:
        """
        Put y into group where x is.
        """
        self._parents[self.find_ancestor(y)] = self.find_ancestor(x)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        MAX_SIZE = max(len(account) for account in accounts) * len(accounts)
        dsu = DSU(MAX_SIZE)

        # Try to union all the emails under each account into the first email
        # of that account.
        seq = 0
        emailToName, emailToId = {}, {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                emailToName[email] = name
                if email not in emailToId:
                    emailToId[email] = seq
                    seq += 1

                dsu.union(emailToId[account[1]], emailToId[email])

        rslt = defaultdict(list)
        for email in emailToName:
            rslt[dsu.find_ancestor(emailToId[email])].append(email)

        return [[emailToName[v[0]]] + sorted(v) for v in rslt.values()]


print(Solution().accountsMerge(
    [
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["John", "johnnybravo@mail.com"],
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["Mary", "mary@mail.com"]]
))
