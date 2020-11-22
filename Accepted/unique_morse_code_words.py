"""
https://leetcode.com/problems/unique-morse-code-words/
"""


from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        memo = dict(zip('abcdefghijklmnopqrstuvwxyz', [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
            "....", "..", ".---", "-.-", ".-..", "--", "-.",
            "---", ".--.", "--.-", ".-.", "...", "-", "..-",
            "...-", ".--", "-..-", "-.--", "--.."]))
        rslt = {
            ''.join(memo[c] for c in w)
            for w in words
        }
        return len(rslt)
