"""
https://leetcode.com/problems/word-break/
"""


from typing import List
from collections import deque


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Using BFS solution.
        """
        visited, queue = set(), deque([0])

        # Get the maximum length of the word in wordDict.
        maxWordLen, n = 0, len(s)
        for w in wordDict:
            maxWordLen = max(maxWordLen, len(w))

        # Find any possible segementations.
        while queue:
            start = queue.popleft()
            if start not in visited:
                for end in range(start + 1, min(start + maxWordLen + 1, n + 1)):
                    if s[start: end] in wordDict:
                        if end == n:
                            return True  # Found a possible segementation.

                        # Continue to search the next segementation.
                        queue.append(end)

                visited.add(start)

        return False


s = 'bb'
wordDict = ['b', 'bbb']
print(Solution().wordBreak(s, wordDict))
