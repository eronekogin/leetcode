"""
https://leetcode.com/problems/maximum-product-of-word-lengths/
"""


from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        """
        Generate a unique mask based on the chars in each word of words.
        Memo is used to store the maximum length of the word per mask.
        Then if two masks x and y are different, x & y should be 0 as each
        bit of x and y is different. Then get the product of such word pair
        lengths and select the maximum one.
        """
        memo, baseVal = {}, ord('a')
        for word in words:
            mask = 0
            for c in set(word):
                mask |= (1 << (ord(c) - baseVal))

            memo[mask] = max(memo.get(mask, 0), len(word))

        return max(
            [
                memo[x] * memo[y]
                for x in memo
                for y in memo
                if not x & y] or [0])
