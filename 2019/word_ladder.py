"""
https://leetcode.com/problems/word-ladder/
"""


from typing import List, Dict, Deque, Tuple
from collections import defaultdict, deque


class Solution:
    def __init__(self):
        self.length = 0
        self.refDict = defaultdict(list)

    def bfs(
            self,
            queue: Deque[Tuple[str, int]],
            topVisited: Dict[str, int],
            bottomVisited: Dict[str, int]) -> int:
        currWord, currLevel = queue.popleft()
        for i in range(self.length):
            key = currWord[:i] + '*' + currWord[i + 1:]
            for nextWord in self.refDict[key]:
                if nextWord in bottomVisited:  # Found the transformation.
                    return currLevel + bottomVisited[nextWord]

                if nextWord not in topVisited:
                    topVisited[nextWord] = currLevel + 1
                    queue.append((nextWord, currLevel + 1))

            self.refDict[key] = []  # Clean the previously checked words.

    def ladderLength(
            self,
            beginWord: str,
            endWord: str,
            wordList: List[str]) -> int:
        """
        Using Bidirectional BFS solution which could reduce the search space.
        """
        if endWord not in wordList:
            return 0

        self.length = len(beginWord)

        # Generarate reference dictionary based on the wordList.
        for w in wordList:
            for i in range(self.length):
                self.refDict[w[:i] + '*' + w[i + 1:]].append(w)

        topQueue, bottomQueue = deque([(beginWord, 1)]), deque([(endWord, 1)])
        topVisited, bottomVisited = {beginWord: 1}, {endWord: 1}
        while topQueue and bottomQueue:
            rslt = self.bfs(topQueue, topVisited, bottomVisited)
            if rslt:
                return rslt

            rslt = self.bfs(bottomQueue, bottomVisited, topVisited)
            if rslt:
                return rslt

        return 0  # No transformation found.
