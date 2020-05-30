"""
https://leetcode.com/problems/reconstruct-original-digits-from-english/
"""


from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        """
        Simply count unique chars in each number word.
        """
        cnt = [0] * 10  # Store the occurrences for each number.
        for c in s:
            if c == 'z':  # Only 'zero' contains 'z'.
                cnt[0] += 1
            elif c == 'w':  # Only 'two' contains 'w'.
                cnt[2] += 1
            elif c == 'u':  # Only 'four' contains 'u'.
                cnt[4] += 1
            elif c == 'x':  # Only 'six' contains 'x'.
                cnt[6] += 1
            elif c == 'g':  # Only 'eight' contains 'g'.
                cnt[8] += 1
            elif c == 'f':  # five + four.
                cnt[5] += 1
            elif c == 's':  # seven + six.
                cnt[7] += 1
            elif c == 'h':  # three + eight.
                cnt[3] += 1
            elif c == 'i':  # nine + five + six + eight.
                cnt[9] += 1
            elif c == 'o':  # one + zero + two + four.
                cnt[1] += 1

        # Reduce duplicate counts.
        cnt[5] -= cnt[4]
        cnt[7] -= cnt[6]
        cnt[3] -= cnt[8]
        cnt[9] -= cnt[5] + cnt[6] + cnt[8]
        cnt[1] -= cnt[0] + cnt[2] + cnt[4]

        return ''.join([str(i) * cnt[i] for i in range(10)])


print(Solution().originalDigits("zeroonetwothreefourfivesixseveneightnine"))
