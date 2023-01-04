"""
https://leetcode.com/problems/maximum-binary-string-after-change/
"""


class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        """
        1. Keep doing operation 2 to modify input string as '000...0111..1'
        2. Then keep doing operation 1 to modify input string to '111..10111..1'
        """
        if '0' not in binary:
            return binary

        ones = binary.count('1', binary.find('0'))
        N = len(binary)
        return '1' * (N - ones - 1) + '0' + '1' * ones


print(Solution().maximumBinaryString('000110'))
