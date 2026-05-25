"""
https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/description/
"""


from heapq import heapify, heappop, heappush


class Solution:
    """
    Solution
    """

    def minimize_string_value(self, s: str) -> str:
        """
        the total cost does not care about where a character is placed,
        as long as a character occurs k times in s, the total cost from
        that character would be 0 + 1 + 2 + ... + k - 2 + k - 1.

        that's why we can sort the assigned to ensure to get the 
        lexicographcailly smallest result.
        """
        cnt = [0] * 26
        offset = ord('a')
        q_indices = []
        for i, c in enumerate(s):
            if c == '?':
                q_indices.append(i)
            else:
                cnt[ord(c) - offset] += 1

        heap = [(x, i) for i, x in enumerate(cnt)]
        heapify(heap)

        assigned = []
        for _ in q_indices:
            f, c = heappop(heap)
            assigned.append(c)
            heappush(heap, (f + 1, c))

        assigned.sort()
        rslt = list(s)
        for i, j in enumerate(q_indices):
            rslt[j] = chr(assigned[i] + offset)

        return ''.join(rslt)
