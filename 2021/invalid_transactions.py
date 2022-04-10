"""
https://leetcode.com/problems/invalid-transactions/
"""


from collections import defaultdict


class Transaction:
    def __init__(self, transaction):
        name, time, amount, city = transaction.split(',')
        self.name = name
        self.time = int(time)
        self.amount = int(amount)
        self.city = city

    def __repr__(self) -> str:
        return ','.join(
            [self.name, str(self.time), str(self.amount), self.city])


class Solution:
    def invalidTransactions(self, transactions: list[str]) -> list[str]:
        transactions: list[Transaction] = list(map(Transaction, transactions))
        transactions.sort(key=lambda t: t.time)
        memo = defaultdict(list)
        for i, t in enumerate(transactions):
            memo[t.name].append(i)

        invalidTransactions = []
        for _, indexes in memo.items():
            l = r = 0
            n = len(indexes)
            for _, index in enumerate(indexes):
                t = transactions[index]
                if (t.amount > 1000):
                    invalidTransactions.append(str(t))
                    continue

                while l <= n - 2 and transactions[indexes[l]].time < t.time - 60:
                    l += 1

                while r <= n - 2 and transactions[indexes[r + 1]].time <= t.time + 60:
                    r += 1

                for i in range(l, r + 1):
                    if transactions[indexes[i]].city != t.city:
                        invalidTransactions.append(str(t))
                        break

        return invalidTransactions


print(Solution().invalidTransactions(
    ["alice,20,800,mtv", "alice,50,1200,mtv"]))
