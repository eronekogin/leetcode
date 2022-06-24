"""
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        currVowels = maxVowels = 0
        for end, c in enumerate(s):
            currVowels += c in 'aeiou'
            if end >= k - 1:
                maxVowels = max(maxVowels, currVowels)
                currVowels -= s[end - k + 1] in 'aeiou'

        return maxVowels


print(Solution().maxVowels("weallloveyou",
                           7))
