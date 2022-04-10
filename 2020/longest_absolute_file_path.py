"""
https://leetcode.com/problems/longest-absolute-file-path/
"""


class Solution:
    def lengthLongestPath(self, inputStr: str) -> int:
        """
        Clarifications:
        1. \n means we are still at the same folder as the previous one.
        2. \t means we are entering a sub folder of the previous one.

        Example:

        1. dir\n(4-space) file.txt

        The longest is "    file.txt", where the file is stored on 
        the same level of dir.

        2. dir\n\t(4-space) file.txt

        The longest is "dir/    file.text", where the file is stored under
        dir. 
        """
        stack = [(-1, 0)]  # (current level, length of the current path)
        foundFile = False
        nextLevel = currLevel = currLen = maxLen = 0
        i, n = 0, len(inputStr)
        while i < n:
            c = inputStr[i]
            if c == '\n':
                # Found a file in the previous item, calculate its path length.
                if foundFile:
                    maxLen = max(maxLen, currLen)
                    foundFile = False

                # Check the level for the next item.
                nextLevel = 0
                while inputStr[i + 1] == '\t':
                    nextLevel += 1
                    i += 1

                if currLevel < nextLevel:  # Go down.
                    currLen += 1  # '/' takes one pisition in the path.
                    stack.append((currLevel, currLen))
                else:  # Stay on the same or go up.
                    while stack[-1][0] >= nextLevel:
                        stack.pop()

                    currLen = stack[-1][-1]

                currLevel = nextLevel
            else:
                if c == '.':
                    foundFile = True

                currLen += 1

            i += 1  # Process the next char.

        if foundFile:  # Process the last file if any.
            maxLen = max(maxLen, currLen)

        return maxLen


print(Solution().lengthLongestPath(
    "file name with  space.txt"))
