"""
https://leetcode.com/problems/random-flip-matrix/
"""


from typing import List
from random import randint


class Solution:
    """
    Use Fisher-Yates shuffle algorithm to pick a random index from the matrix.
    The Fisher-Yates shuffle generally does the following steps:
    1. Pick a random number from [1, N], then swap the number with the last
        number N. The possibility of picking that number is 1/N.
    2. Then pick a random number from [1, N - 1], then swap the number with the
        last number N - 1. The possibility of picking that number is
        (1/(N-1) * (1- 1/N)) = 1/(N-1)*(N-1)/N = 1/N. 
    3. Repeat until the last number is picked out.

    With this algorithm we only need to call randint once in the flip function.
    """

    def __init__(self, n_rows: int, n_cols: int):
        self.R = n_rows
        self.C = n_cols
        self.maxIdx = n_rows * n_cols - 1
        self.memo = {}  # {current index: actual value}

    def flip(self) -> List[int]:
        maxIdx, memo = self.maxIdx, self.memo
        # Pick a random index.
        i = randint(0, maxIdx)

        # Store the actual value matching the index i for return purpose.
        actualPosition = memo.get(i, i)

        # Swap it with the number at the tail of the current sequence.
        memo[i], memo[maxIdx] = memo.get(maxIdx, maxIdx), actualPosition

        # Reduce total for the future pick.
        self.maxIdx = maxIdx - 1

        # Return the actual row and column number back.
        return list(divmod(actualPosition, self.C))

    def reset(self) -> None:
        """
        No need to reset the current sequence in the memo back to 0, 1, ... N
        as the current random sequence is good enough for the future pick up.
        """
        self.maxIdx = self.R * self.C - 1


s = Solution(1, 2)
s.flip()
s.flip()
s.reset()
s.flip()
