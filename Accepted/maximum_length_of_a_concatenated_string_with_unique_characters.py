"""
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
"""


class Solution:
    def maxLength(self, arr: list[str]) -> int:
        dp = [set()]
        for w in arr:
            if len(set(w)) < len(w):  # Skip word having duplicate chars.
                continue

            sw = set(w)
            for combination in dp[:]:
                # Skip if the current word has conflict chars.
                if sw & combination:
                    continue

                dp.append(sw | combination)

        return max(len(combination) for combination in dp)
