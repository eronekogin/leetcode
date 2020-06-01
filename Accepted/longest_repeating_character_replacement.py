"""
https://leetcode.com/problems/longest-repeating-character-replacement/
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Using sliding window solution:

        1. maxOccurrences hold the maximum occurrences among the unique chars
            in the current window.
        2. ops = maxLen - maxOccurrences means the number of replacements we 
            need to make in the current window to make all chars repeating.
        3. When ops < k, we could make more replacements, so we expand the
            current window.
        4. When ops >= k, we could make no more replacement, so we remove the
            leading char from the current window. In other words, we slide
            the current window to the right by one char.
        5. The only case we could expand our window's size is when the next
            char's total occurrences in the current window is greater than the
            previous maxOccurrence, otherwise we keep sliding the window to
            the right side as we cannot form a larger window from the current
            starting position.
        6. Since we never shrink our sliding window, when reaching the end of
            s, we get our longest window.
        """
        maxLen, maxOccurrences = 0, 0
        cnt = {}
        for i, c in enumerate(s):
            cnt[c] = cnt.get(c, 0) + 1
            maxOccurrences = max(maxOccurrences, cnt[c])
            if maxLen - maxOccurrences < k:
                maxLen += 1
            else:
                delChar = s[i - maxLen]
                cnt[delChar] -= 1

        return maxLen
