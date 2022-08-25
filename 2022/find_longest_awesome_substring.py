"""
https://leetcode.com/problems/find-longest-awesome-substring/
"""


class Solution:
    def longestAwesome(self, s: str) -> int:
        """
        1. A palindrom string can be formed by a string composed with the
            count for all chars are even or the count for one char is odd and
            the remaining is even.
        2. Then we could use bitmask to collect the total counter of each
            chars. When one bit is set to 1, it means the current counter of
            this char is odd and when one bit is set to zero, it means the
            current counter of this char is even.
        3. Then we count prefix xors for such bit masks, then for each bit
            mask that occurs again, the counter of the substring between 
            this one and the previous one are all even, which meas they could
            form a palindrome.
        4. Since we are going to find the maximum sized subtring, we will keep
            the position where each unique mask occurs the first time.
        """
        maxLen, N = 0, len(s)
        currMask = 0
        minStarts = [-1] + [N] * ((1 << 10) - 1)
        for end, c in enumerate(s):
            currMask ^= (1 << int(c))

            # Use any number as the middle odd count char, then check if the
            # bit mask is seen before.
            for num in range(10):
                maxLen = max(
                    maxLen,
                    end - minStarts[currMask ^ (1 << num)]
                )

            # No odd char, check if the current mask occurs before.
            maxLen = max(
                maxLen,
                end - minStarts[currMask]
            )

            minStarts[currMask] = min(minStarts[currMask], end)

        return maxLen
