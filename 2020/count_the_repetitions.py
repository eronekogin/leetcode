"""
https://leetcode.com/problems/count-the-repetitions/
"""


class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        """
        The reason why the idxs' length is len(s2) + 1 is because for a start
        index of s2 at each start of s1, it could have 0 to len(s2) - 1 values,
        which is len(s2), if we have scanned len(s2) + 1 times of s1, there
        must be at least one bucket which holds more than 1 item according to
        pigeon hole principle.
        """
        if not n1:  # s1 repeat zero times.
            return 0

        maxLen = len(s2)
        idxs = [0] * (maxLen + 1)  # index of s2 at each start of s1.
        cnts = [0] * (maxLen + 1)  # count of s2 at each start of s1.
        idx = count = 0
        for i in range(n1):
            for c in s1:
                if c == s2[idx]:
                    idx += 1

                if idx == maxLen:  # Found a s2 in s1.
                    idx = 0
                    count += 1

            idxs[i], cnts[i] = idx, count
            for k in range(i):
                if idxs[k] == idx:  # Found a repeat pattern.
                    prevCnt = cnts[k]
                    patternCnt = (cnts[i] - cnts[k]) * \
                        ((n1 - 1 - k) // (i - k))
                    remainCnt = cnts[k + (n1 - 1 - k) % (i - k)] - cnts[k]

                    return (prevCnt + patternCnt + remainCnt) // n2

        # If found no repeat pattern.
        return cnts[n1 - 1] // n2
