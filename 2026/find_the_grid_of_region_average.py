"""
https://leetcode.com/problems/find-the-grid-of-region-average/description/
"""


class Solution:
    """
    Solution
    """

    def result_grid(self, image: list[list[int]], threshold: int) -> list[list[int]]:
        """
        result grid
        """
        def get_region_avg(r: int, c: int) -> int:
            if r + 3 > m or c + 3 > n:
                return -1

            total = 0
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    v = image[i][j]
                    if i + 1 < r + 3 and abs(v - image[i + 1][j]) > threshold:
                        return -1

                    if j + 1 < c + 3 and abs(v - image[i][j + 1]) > threshold:
                        return -1

                    total += v

            return total // 9

        m, n = len(image), len(image[0])
        memo: dict[tuple[int, int], list[int]] = {}

        for r in range(m):
            for c in range(n):
                avg = get_region_avg(r, c)
                if avg >= 0:
                    for i in range(r, r + 3):
                        for j in range(c, c + 3):
                            if (i, j) not in memo:
                                memo[(i, j)] = []

                            memo[(i, j)].append(avg)

        rslt = [[0] * n for _ in range(m)]
        for r, row in enumerate(image):
            for c, v in enumerate(row):
                intensities = memo.get((r, c), [])
                if intensities:
                    rslt[r][c] = sum(intensities) // len(intensities)
                else:
                    rslt[r][c] = v

        return rslt


print(Solution().result_grid(
    [[5, 6, 7, 10], [8, 9, 10, 10], [11, 12, 13, 10]], 3))
