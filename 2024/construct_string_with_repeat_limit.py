"""
https://leetcode.com/problems/construct-string-with-repeat-limit/description/
"""


from heapq import heappush, heappop, heapify
from collections import Counter


class Solution:
    """
    Solution
    """

    def repeat_limited_string(self, s: str, repeat_limit: int) -> str:
        """
        repeat limited string
        """
        heap = [(-ord(c), v) for c, v in Counter(s).items()]
        heapify(heap)

        rslt: list[int] = []
        while heap:
            k, v = heappop(heap)
            if rslt and rslt[-1] == k:
                # Previous limit reached, check the next key.
                if not heap:
                    break

                nk, nv = heappop(heap)
                rslt.append(nk)

                if nv > 1:
                    heappush(heap, (nk, nv - 1))

                heappush(heap, (k, v))  # Push back the current key
            else:
                m = min(repeat_limit, v)
                rslt.extend([k] * m)
                if v > m:
                    heappush(heap, (k, v - m))

        return ''.join(chr(-x) for x in rslt)
