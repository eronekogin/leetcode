"""
https://leetcode.com/problems/substring-with-concatenation-of-all-words/
"""

from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        Easy to understand version.
        """
        totalWords, totalLen = len(words), len(s)
        if totalWords == 0:
            return []

        wordLen = len(words[0])  # Each word in words have the same length.
        interval = totalWords * wordLen
        if totalLen < interval:
            return []

        # Create max counter dicitonary.
        maxCntDict = {}
        for word in words:
            maxCntDict[word] = maxCntDict.get(word, 0) + 1

        # Calculate result.
        i, rslt, cntDict = 0, [], {}
        while i + interval <= totalLen:
            isFound = True
            for j in range(i, i + interval, wordLen):
                chkWord = s[j: j + wordLen]
                cntDict[chkWord] = cntDict.get(chkWord, 0) + 1
                if cntDict[chkWord] > maxCntDict.get(chkWord, 0):
                    isFound = False
                    break

            if isFound:
                rslt.append(i)

            i += 1  # Process the next char.
            cntDict.clear()  # Empty the counter dictionary.

        return rslt

    def findSubstring2(self, s: str, words: List[str]) -> List[int]:
        """
        Optimized solution without empty the counter dictionary every time.
        """
        totalWords, totalLen = len(words), len(s)
        if totalWords == 0:
            return []

        wordLen = len(words[0])  # Each word in words have the same length.
        if totalLen < totalWords * wordLen:
            return []

        # Create max counter dicitonary.
        maxCntDict = {}
        for word in words:
            maxCntDict[word] = maxCntDict.get(word, 0) + 1

        # Calculate rslt.
        cntDict, rslt = {}, []
        """
        Having a window with length as totalWords * wordLen, put the window 
        to a start point in s. Then after each check, move the window to the 
        next position = current position + wordLen. With that in mind, the
        valid start point in s should be [0, wordLen - 1], as if we start
        from wordLen, it is already checked in the round when the start point
        is 0.
        """
        for i in range(wordLen):
            left, wordCnt = i, 0
            for right in range(i, totalLen, wordLen):
                chkWord = s[right: right + wordLen]
                if chkWord not in words:
                    # Current check word is not valid, move right
                    # to the next word and clear counter dictionary.
                    left, wordCnt = right + wordLen, 0
                    cntDict.clear()
                else:
                    wordCnt += 1  # Found a valid word.
                    cntDict[chkWord] = cntDict.get(chkWord, 0) + 1
                    while cntDict[chkWord] > maxCntDict[chkWord]:
                        # Current check word exceeds its max counter,
                        # move left until the counter of chkWord is
                        # less than the max counter.
                        cntDict[s[left: left + wordLen]] -= 1
                        wordCnt -= 1
                        left += wordLen

                    if wordCnt == totalWords:  # Found a valid substring.
                        rslt.append(left)
                        wordCnt -= 1  # Remove the word from counter dict.
                        cntDict[s[left: left + wordLen]] -= 1
                        left += wordLen  # Move left to the next word.

            cntDict.clear()  # Clear counter dict for the next start position.

        return rslt


print(Solution().findSubstring2(
    'barfoothefoobarman', ['foo', 'bar']))
