"""
https://leetcode.com/problems/longest-uploaded-prefix/description/
"""


class LUPrefix:
    """
    LUPrefix
    """

    def __init__(self, n: int):
        self.videos: list[int] = [0] * (n + 1)
        self.prefix = 0

    def upload(self, video: int) -> None:
        """
        upload
        """
        self.videos[video - 1] = 1

    def longest(self) -> int:
        """
        longest
        """
        while self.videos[self.prefix]:
            self.prefix += 1

        return self.prefix


l = LUPrefix(4)
l.upload(3)
l.upload(1)
l.upload(2)
