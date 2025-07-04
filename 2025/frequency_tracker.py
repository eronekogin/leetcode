"""
https://leetcode.com/problems/frequency-tracker/description/
"""


class FrequencyTracker:
    """
    Frequency Tracker
    """

    def __init__(self):
        self.memo: dict[int, int] = {}
        self.freqs: dict[int, int] = {}

    def add(self, number: int) -> None:
        """
        add
        """
        f = self.memo.get(number, 0)
        self.memo[number] = f + 1
        self.freqs[f] = max(self.freqs.get(f, 0) - 1, 0)
        self.freqs[f + 1] = self.freqs.get(f + 1, 0) + 1

    def delete_one(self, number: int) -> None:
        """
        delete one
        """
        if number in self.memo:
            f = self.memo[number]
            self.memo[number] = max(f - 1, 0)
            self.freqs[f] -= 1
            self.freqs[f - 1] = self.freqs.get(f - 1, 0) + 1

    def has_frequency(self, frequency: int) -> bool:
        """
        has frequency
        """
        return self.freqs.get(frequency, 0) > 0
