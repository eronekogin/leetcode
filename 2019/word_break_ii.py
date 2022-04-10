"""
https://leetcode.com/problems/word-break-ii/
"""


from typing import List, Set
from collections import deque


class Solution:
    def __init__(self):
        # self.ref[i] stands for all the words combination of wordDict
        # in order to form the string s[:i].
        self.ref = None

    def gen_ref(self, s: str, wordSet: Set[str]):
        # Get maximum length of the words in wordSet.
        maxLen, n = 0, len(s) + 1
        for w in wordSet:
            maxLen = max(maxLen, len(w))

        # Search for any possible combinations positions.
        self.ref = [[] for _ in range(n)]
        self.ref[0] = True
        for end in range(n):
            for start in range(max(0, end - maxLen), end):
                w = s[start:end]
                if self.ref[start] and w in wordSet:
                    self.ref[end].append(w)

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.gen_ref(s, set(wordDict))
        n = len(s)
        rslt, queue = [], deque([(n, [])])
        while queue:
            currEnd, currPath = queue.popleft()
            # Walk through each possible path.
            for w in self.ref[currEnd]:
                if currEnd == len(w):
                    rslt.append(' '.join([w] + currPath))
                else:
                    queue.append((currEnd - len(w), [w] + currPath))

        return rslt


s = 'leetcode'
wordDict = ['leet', 'code']
print(Solution().wordBreak(s, wordDict))
