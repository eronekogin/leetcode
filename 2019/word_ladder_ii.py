"""
https://leetcode.com/problems/word-ladder-ii/
"""


from typing import List, Dict, Tuple, Set
from collections import defaultdict
from string import ascii_lowercase


class Solution:
    def __init__(self):
        self.length = 0
        self.refDict = defaultdict(set)
        self.topLayer = set()
        self.topPaths = defaultdict(set)
        self.topVisited = set()
        self.bottomLayer = set()
        self.bottomPaths = defaultdict(set)
        self.bottomVisited = set()

    def gen_path(
            self,
            pathTable: Dict[str, Set[str]],
            start: str,
            end: str) -> List[List[str]]:
        rslt = []
        if start == end:
            return [[end]]

        for word in pathTable[end]:
            for path in self.gen_path(pathTable, start, word):
                rslt.append(path + [end])

        return rslt

    def _gen_refs(self, wordList: List[List[str]]):
        for w in wordList:
            for i in range(self.length):
                self.refDict[w[:i] + '*' + w[i + 1:]].add(w)

    def bfs_search(
            self,
            currLayer: Set[str],
            pathTable: Dict[str, Set[str]],
            visited: Set[str]) -> Set[str]:
        nextLayer = set()
        for currWord in currLayer:
            for i in range(self.length):
                key = currWord[:i] + '*' + currWord[i + 1:]
                for nextWord in self.refDict[key]:
                    if nextWord not in visited:
                        pathTable[nextWord].add(currWord)
                        nextLayer.add(nextWord)

        visited.update(nextLayer)
        return nextLayer

    def findLadders(
            self,
            beginWord: str,
            endWord: str,
            wordList: List[str]) -> List[List[str]]:
        """
        Using bidirectional BFS solution which could reduce search space.
        """
        if endWord not in wordList:
            return []

        self.length = len(beginWord)
        self._gen_refs(wordList)
        self.topLayer, self.topVisited = {beginWord}, {beginWord}
        self.bottomLayer, self.bottomVisited = {endWord}, {endWord}
        while self.topLayer and self.bottomLayer:
            if self.topVisited & self.bottomVisited:
                break

            self.topLayer = self.bfs_search(
                self.topLayer, self.topPaths, self.topVisited)

            if self.topVisited & self.bottomVisited:
                break

            self.bottomLayer = self.bfs_search(
                self.bottomLayer, self.bottomPaths, self.bottomVisited)

        return [
            top + end[::-1][1:]
            for mid in self.topLayer & self.bottomLayer
            for top in self.gen_path(self.topPaths, beginWord, mid)
            for end in self.gen_path(self.bottomPaths, endWord, mid)
        ]


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(Solution().findLadders(beginWord, endWord, wordList))
