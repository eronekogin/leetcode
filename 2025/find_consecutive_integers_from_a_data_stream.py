"""
https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/description/
"""


class DataStream:
    """
    data stream
    """

    def __init__(self, value: int, k: int):
        self.cnt = 0
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        """
        consec
        """
        if num == self.value:
            self.cnt += 1
        else:
            self.cnt = 0

        return self.cnt == self.k
