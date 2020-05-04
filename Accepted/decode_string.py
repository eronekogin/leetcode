"""
https://leetcode.com/problems/decode-string/
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack, pre, curr = [], [], []
        repeatTimes = 0
        for c in s:
            if c.isdecimal():
                repeatTimes = repeatTimes * 10 + int(c)
            elif c == '[':
                stack.append((curr, repeatTimes))
                curr = []
                repeatTimes = 0
            elif c == ']':
                pre, repeatTimes = stack.pop()
                curr = pre + curr * repeatTimes
                repeatTimes = 0
            else:
                curr.append(c)

        return ''.join(curr)


s = "10[a20[b]]"
print(Solution().decodeString(s))
