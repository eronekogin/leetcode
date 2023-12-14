"""
https://leetcode.com/problems/process-restricted-friend-requests/
"""


class Solution:
    """
    Solution
    """

    def friend_requests(
        self, n: int,
        restrictions: list[list[int]],
        requests: list[list[int]]
    ) -> list[bool]:
        """
        friend_requests
        """
        def find(i):
            if i != uf[i]:
                uf[i] = find(uf[i])
            return uf[i]

        uf = {i: i for i in range(n)}
        res = []

        for i, j in requests:
            success = True
            pi, pj = find(i), find(j)
            if pi != pj:
                for x, y in restrictions:
                    px, py = find(x), find(y)
                    if (px, py) == (pi, pj) or (px, py) == (pj, pi):
                        success = False
                        break
            if success:
                uf[pj] = pi
            res.append(success)
        return res
