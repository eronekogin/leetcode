"""
https://leetcode.com/problems/maximum-score-of-a-node-sequence/description/
"""


from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    """
    Solution
    """

    def maximum_score(self, scores: list[int], edges: list[list[int]]) -> int:
        """
        maximum score
        """
        def get_top_3(a: int, b: int) -> None:
            heap = top3[a]
            heappush(heap, (scores[b], b))
            if len(heap) > 3:
                heappop(heap)

        top3: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)
        for a, b in edges:
            get_top_3(a, b)
            get_top_3(b, a)

        rslt = -1
        for a, b in edges:
            if len(top3[a]) < 2 or len(top3[b]) < 2:
                continue

            for na in top3[a]:
                for nb in top3[b]:
                    if na[1] not in (a, b) and nb[1] not in (a, b) and na[1] != nb[1]:
                        rslt = max(
                            rslt,
                            scores[a] + scores[b] + na[0] + nb[0]
                        )

        return rslt
