"""
https://leetcode.com/problems/maximum-frequency-stack/
"""


from collections import Counter, defaultdict


class FreqStack:

    def __init__(self):
        self.freqs = Counter()
        self.freqGroups = defaultdict(list)
        self.maxFreq = 0

    def push(self, x: int) -> None:
        newFreq = self.freqs[x] + 1
        self.freqs[x] = newFreq
        if newFreq > self.maxFreq:
            self.maxFreq = newFreq

        self.freqGroups[newFreq].append(x)

    def pop(self) -> int:
        x = self.freqGroups[self.maxFreq].pop()
        self.freqs[x] -= 1
        if not self.freqGroups[self.maxFreq]:
            self.maxFreq -= 1

        return x
