"""
https://leetcode.com/problems/filling-bookcase-shelves/
"""


class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        """
        1. Suppose dp[i] stands for the minimum height we could get by placing
            the first i - 1 books on the shelf.
        2. Then for the ith book, we either put it on the new row, or grab
            the books from the previous rows and put it together with the
            i+1 th book, so we have:
            dp[i + 1] = min(
                dp[i] + height[i],
                dp[j] + max(height[j: i + 1] while sum(
                    width[j: i + 1] <= shelfWidth))
            )
        """
        N = len(books)
        dp = [0] * (N + 1)
        for i in range(1, N + 1):
            width, height = books[i - 1]
            dp[i] = dp[i - 1] + height
            totalWidth = width
            j = i - 1
            maxHeight = height
            while j > 0 and books[j - 1][0] + totalWidth <= shelfWidth:
                maxHeight = max(maxHeight, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + maxHeight)
                totalWidth += books[j - 1][0]
                j -= 1

        return dp[-1]


print(Solution().minHeightShelves(
    [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4))
