"""
https://leetcode.com/problems/count-binary-substrings/
"""


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cnt = preCnt = 0
        currCnt = 1
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                cnt += min(preCnt, currCnt)
                preCnt, currCnt = currCnt, 1
            else:
                currCnt += 1

        return cnt + min(preCnt, currCnt)


print(Solution().countBinarySubstrings('10101'))
