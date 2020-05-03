"""
https://leetcode.com/problems/utf-8-validation/
"""


from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        m1, m2 = 1 << 7, 1 << 6
        totalBytes = 0
        for num in data:
            if totalBytes:  # Check if the following bytes are valid.
                if not num & m1 or num & m2:  # Must be 10xxxxxx.
                    return False
            else:
                m = m1
                while num & m:  # Count how many bytes this unicode takes.
                    totalBytes += 1
                    m >>= 1

                if totalBytes == 1 or totalBytes > 4:
                    return False

            if totalBytes:  # Skip checking when the unicode takes just 1 byte.
                totalBytes -= 1

        return not totalBytes


print(Solution().validUtf8([197, 130, 1]))
