"""
https://leetcode.com/problems/longest-happy-string/
"""


from heapq import heappush, heappop, heapreplace


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []

        # Initialize.
        for count, token in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count:
                heappush(heap, (count, token))

        rslt = []
        while heap:
            count, token = heappop(heap)
            if len(rslt) > 1 and rslt[-2] == rslt[-1] == token:
                # Should avoid three consecutive same tokens.
                if not heap:
                    break

                # Use the token that is currently at the top of the heap,
                # then pushback the original popped token.
                count, token = heapreplace(heap, (count, token))

            rslt.append(token)
            if count + 1 < 0:  # Still have unused token.
                heappush(heap, (count + 1, token))

        return ''.join(rslt)
