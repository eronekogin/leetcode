"""
https://leetcode.com/problems/text-justification/
"""

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        rslt, line = [], []
        currWidth = 0
        for word in words:
            currWords, currWordLen = len(line), len(word)
            if currWidth + currWordLen + currWords > maxWidth:
                # The current line cannot hold more word.
                # Use round robin algrithm to distribute
                # the spaces on the current line.
                for i in range(maxWidth - currWidth):
                    line[i % (currWords - 1 or 1)] += ' '

                rslt.append(''.join(line))
                line.clear()
                currWidth = 0

            currWidth += currWordLen
            line.append(word)

        # The last line does not have any extra space.
        rslt.append(' '.join(line).ljust(maxWidth))
        return rslt


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(Solution().fullJustify(words, maxWidth))
