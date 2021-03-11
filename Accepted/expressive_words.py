"""
https://leetcode.com/problems/expressive-words/
"""


class Solution:
    def expressiveWords(self, S: str, words: list[str]) -> int:
        def compress(w: str) -> list[list[str, int]]:
            if not w:
                return []

            rslt = [[w[0], 1]]
            for i in range(1, len(w)):
                if w[i] != w[i - 1]:
                    rslt.append([w[i], 1])
                else:
                    rslt[-1][-1] += 1

            return rslt

        cs = compress(S)
        stretchyWords = 0
        for w in words:
            cw = compress(w)
            if len(cs) == len(cw):
                found = 1
                for (t, check) in zip(cs, cw):
                    if check[0] != t[0] or check[1] > t[1] or \
                            (check[1] < t[1] and t[1] < 3):
                        found = 0
                        break

                stretchyWords += found

        return stretchyWords


print(Solution().expressiveWords("heeellooo", ["hello", "hi", "helo"]))
