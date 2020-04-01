"""
https://leetcode.com/problems/reverse-vowels-of-a-string/
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s:
            return s

        vowels = set('aeiouAEIOU')
        sl = list(s)
        left, right = 0, len(s) - 1
        while True:
            while sl[left] not in vowels and left < right:
                left += 1

            while sl[right] not in vowels and left < right:
                right -= 1

            if left < right:
                sl[left], sl[right] = sl[right], sl[left]
                left += 1
                right -= 1
            else:
                break

        return ''.join(sl)


print(Solution().reverseVowels('hello'))
