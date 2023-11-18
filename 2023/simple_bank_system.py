"""
https://leetcode.com/problems/simple-bank-system/
"""


class Bank:
    """
    Bank
    """

    def __init__(self, balance: list[int]):
        self.accounts = balance
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        """
        transfer
        """
        if not (1 <= account1 <= self.n and 1 <= account2 <= self.n):
            return False

        if self.accounts[account1 - 1] >= money:
            self.accounts[account1 - 1] -= money
            self.accounts[account2 - 1] += money
            return True

        return False

    def deposit(self, account: int, money: int) -> bool:
        """
        deposit
        """
        if not 1 <= account <= self.n:
            return False

        self.accounts[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        """
        withdraw
        """
        if not 1 <= account <= self.n:
            return False

        if self.accounts[account - 1] >= money:
            self.accounts[account - 1] -= money
            return True

        return False
