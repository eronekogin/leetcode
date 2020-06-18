"""
https://leetcode.com/problems/string-compression/
"""


from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0

        compressedStart = 0
        cnt, preChar = 0, chars[0]
        for currChar in chars:
            if currChar != preChar:
                preChar = currChar
                compressedStart += 1
                if cnt > 1:  # Store counter next to the previous char.
                    for c in str(cnt):
                        chars[compressedStart] = c
                        compressedStart += 1

                chars[compressedStart] = currChar
                cnt = 1
            else:
                cnt += 1

        # Process the last one.
        compressedStart += 1
        if cnt > 1:  # Store counter next to the previous char.
            for c in str(cnt):
                chars[compressedStart] = c
                compressedStart += 1

        return compressedStart


print(Solution().compress(["a", "a", "b", "b", "c", "c", "c"]))
