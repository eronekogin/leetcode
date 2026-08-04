"""
https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/description/
"""


from heapq import heappop, heappush


class Solution:
    """
    Solution
    """

    def clear_stars(self, s: str) -> str:
        """
        clear stars
        """
        chars = list(s)
        heap: list[tuple[int, int]] = []
        for i, c in enumerate(chars):
            if c == '*':
                if heap:
                    _, j = heappop(heap)
                    chars[-j] = ''
                    chars[i] = ''
            else:
                heappush(heap, (ord(c), -i))

        return ''.join(chars)
