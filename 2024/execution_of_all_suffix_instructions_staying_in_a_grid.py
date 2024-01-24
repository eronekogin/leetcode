"""
https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/description/
"""


class Solution:
    """
    Solution
    """

    def execute_instructions(self, n: int, start_pos: list[int], s: str) -> list[int]:
        """
        execute_instructions
        """
        def execute(start: int):
            r, c = start_pos
            end = start
            while end < m:
                if s[end] == 'L':
                    c -= 1
                elif s[end] == 'R':
                    c += 1
                elif s[end] == 'U':
                    r -= 1
                else:
                    r += 1

                if r < 0 or r >= n or c < 0 or c >= n:
                    break

                end += 1

            return end - start

        m = len(s)
        return [execute(i) for i in range(len(s))]


print(Solution().execute_instructions(3, [0, 1], "RRDDLU"))
