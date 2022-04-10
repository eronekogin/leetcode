"""
https://leetcode.com/problems/longest-common-prefix/
"""


class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if len(strs) == 0:
            return ''

        # The first element, set result to itself.
        rIdx = len(strs[0])

        for cnt in range(1, len(strs)):
            # Calculate the longest common prefix.
            checkIdx = min(rIdx, len(strs[cnt]))
            rIdx = 0

            while rIdx < checkIdx and strs[0][rIdx] == strs[cnt][rIdx]:
                rIdx += 1

            if rIdx == 0:  # No match at all.
                return ''

        return strs[0][0: rIdx]


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
