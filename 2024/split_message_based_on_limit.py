"""
https://leetcode.com/problems/split-message-based-on-limit/description/
"""


class Solution:
    """
    Solution
    """

    def split_message(self, message: str, limit: int) -> list[str]:
        """
        split message
        """
        total_indexes_len = 0
        max_parts = 0
        n = len(message)

        while (
            3 + len(str(max_parts)) * 2 < limit and
            (
                total_indexes_len +
                n +
                (3 + len(str(max_parts))) * max_parts
            ) > limit * max_parts
        ):
            max_parts += 1
            total_indexes_len += len(str(max_parts))

        if 3 + len(str(max_parts)) * 2 >= limit:
            return []

        rslt: list[str] = []
        i = 0
        base_index_str = str(max_parts)
        base_index_len = len(base_index_str)
        for j in range(1, max_parts + 1):
            offset = limit - (len(str(j)) + 3 + base_index_len)
            rslt.append(f'{message[i: i + offset]}<{str(j)}/{base_index_str}>')
            i += offset

        return rslt
