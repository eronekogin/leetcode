"""
https://leetcode.com/problems/next-greater-numerically-balanced-number/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def next_beautiful_number(self, n: int) -> int:
        """
        next_beautiful_number
        """
        def backtracking(i: int, num_len: int, curr_num: int, counter: Counter):
            if i == num_len:
                is_candidate = True
                for d, freq in counter.items():
                    if freq != 0 and d != freq:
                        is_candidate = False

                if is_candidate:
                    yield curr_num

                return

            for d in range(1, num_len + 1):
                if counter[d] >= d or counter[d] + num_len - i < d:
                    # Need more number or not enough place to put all number
                    continue

                counter[d] += 1
                yield from backtracking(i + 1, num_len, curr_num * 10 + d, counter)
                counter[d] -= 1

        for num_len in range(len(str(n)), len(str(n)) + 2):
            for num in backtracking(0, num_len, 0, Counter()):
                if num > n:
                    return num

        return -1  # Not possible.
