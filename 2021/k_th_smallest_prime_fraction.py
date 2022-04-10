"""
https://leetcode.com/problems/k-th-smallest-prime-fraction/
"""


from bisect import bisect_right


class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        """
        Suppose we have a N x N matrix with N as the length of the given
        list and matrix[r][c] = arr[r] / arr[N - 1 - c], then in the end
        we will have a matrix with each row and each column in ascending
        order. Now we have transformed our question into find the kth
        smallest element in this matrix, then we could apply binary search.
        """
        # Since arr is already sorted in ascending order and we only consider
        # fractions with arr[i] / arr[j] when i < j, then our search space
        # will be limited to (0, 1).
        start, end, N = 0, 1, len(arr)

        while True:
            m = (start + end) / 2
            # For each row, we need to find the total number of elements less
            # than m. In other words, if arr[r] / arr[N - 1 - c] < m,
            # It means arr[r] / m < arr[N - 1 - c]. So if we do a binary
            # search in arr to find all the index of the first number that is
            # greater than arr[r] / m, say i, then the total number of
            # elements less than m will be N - i, with arr[r] / arr[i] as the
            # maximum fraction on each row.
            boarders = [bisect_right(arr, arr[r] / m) for r in range(N)]
            total = sum(N - i for i in boarders)
            if total > k:  # Too many numbers.
                end = m
            elif total < k:  # Too few numbers.
                start = m
            else:  # Exactly k numbers.
                # Then we need to find the maximum fraction as our answer. The
                # current maximum fraction is the maximum fraction generated
                # from those boarders. Notice we should only consider the
                # boarder with less than N as if it is N, it means the whole
                # row is greater than the current m.
                return max(
                    [
                        (arr[r], arr[i])
                        for r, i in enumerate(boarders)
                        if i < N
                    ],
                    key=lambda x: x[0] / x[1])
