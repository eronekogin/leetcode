"""
https://leetcode.com/problems/find-and-replace-in-string/
"""


class Solution:
    def findReplaceString(
            self, S: str,
            indexes: list[int],
            sources: list[str],
            targets: list[str]) -> str:
        rslt = []
        memo = {
            indexes[i]: (sources[i], targets[i]) for i in range(len(indexes))}
        i = 0
        while i < len(S):
            if i in memo:
                src, target = memo[i]
                if S[i: i + len(src)] == src:
                    rslt.append(target)
                    i += len(src)
                else:
                    rslt.append(S[i])
                    i += 1
            else:
                rslt.append(S[i])
                i += 1

        return ''.join(rslt)


print(Solution().findReplaceString("abcd",
                                   [0, 2],
                                   ["a", "cd"],
                                   ["eee", "ffff"]))
