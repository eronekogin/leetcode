"""
https://leetcode.com/problems/most-frequent-prime/description/
"""


from itertools import product


class Solution:
    """
    Solution
    """

    def most_frequent_prime(self, mat: list[list[int]]) -> int:
        """
        most frequent prime
        """
        def is_prime(x: int) -> bool:
            if x < 10 or x % 2 == 0:
                return False

            for i in range(3, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False

            return True

        m, n = len(mat), len(mat[0])
        d = (-1, 0, 1)
        cnt: dict[int, int] = {}

        for r, c, dr, dc in product(range(m), range(n), d, d):
            if dr == 0 == dc:
                continue

            nr, nc = r + dr, c + dc
            curr = mat[r][c]
            while 0 <= nr < m and 0 <= nc < n:
                curr = curr * 10 + mat[nr][nc]
                cnt[curr] = cnt.get(curr, 0) + 1
                nr += dr
                nc += dc

        candidates = [x for x in cnt if is_prime(x)]
        if not candidates:
            return -1

        candidates.sort(key=lambda x: (cnt[x], x), reverse=True)
        return candidates[0]
