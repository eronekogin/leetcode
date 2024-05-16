"""
https://leetcode.com/problems/design-an-atm-machine/description/
"""


class ATM:
    """
    ATM
    """

    def __init__(self):
        self.banknotes: list[int] = [0] * 5
        self.mappings = [20, 50, 100, 200, 500]

    def deposit(self, banknotes_count: list[int]) -> None:
        """
        deposit
        """
        for i, v in enumerate(banknotes_count):
            self.banknotes[i] += v

    def withdraw(self, amount: int) -> list[int]:
        """
        withdraw
        """
        rslt: list[int] = []
        remain_amt = amount
        for money, cnt in zip(self.mappings[::-1], self.banknotes[::-1]):
            need = min(cnt, remain_amt // money)
            rslt = [need] + rslt
            remain_amt -= need * money

        if remain_amt > 0:  # Not enough notes
            return [-1]

        # Found a match, deduct the required notes from bank
        self.deposit([-x for x in rslt])

        return rslt


atm = ATM()
atm.deposit([250796, 638723, 691758, 845522, 938973])
atm.deposit([215317, 848628, 182949, 784609, 30472])
atm.withdraw(701035245)
atm.withdraw(109992310)
atm.withdraw(755819795)
atm.withdraw(722349970)
