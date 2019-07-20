"""
https://leetcode.com/problems/count-and-say/
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        currStr = '1'  # Case: n = 1.

        rslt = []
        for _ in range(n - 1):  # Loop n - 1 times.
            preChar, cnt = currStr[0], 0
            for c in currStr:
                if c != preChar:
                    rslt.append(str(cnt))
                    rslt.append(preChar)
                    preChar = c
                    cnt = 1
                else:
                    cnt += 1

            # Append the last item.
            rslt.append(str(cnt))
            rslt.append(preChar)
            currStr = ''.join(rslt)
            rslt.clear()

        return currStr


s = Solution()

for i in range(1, 11):
    print('{0}: {1}'.format(i, s.countAndSay(i)))
