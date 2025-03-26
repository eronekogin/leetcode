"""
https://leetcode.com/problems/count-vowel-strings-in-ranges/description/
"""


from itertools import accumulate


class Solution:
    """
    Solution
    """

    def vowel_strings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        """
        vowel strings
        """
        vowels = set('aeiou')
        candidates = [w[0] in vowels and w[-1] in vowels for w in words]
        prefix_sums = list(accumulate(candidates, initial=0))
        return [
            prefix_sums[j + 1] - prefix_sums[i]
            for i, j in queries
        ]


print(Solution().vowel_strings(
    ["bzmxvzjxfddcuznspdcbwiojiqf",
     "mwguoaskvramwgiweogzulcinycosovozppl",
     "uigevazgbrddbcsvrvnngfrvkhmqszjicpieahs",
     "uivcdsboxnraqpokjzaayedf",
     "yalc",
     "bbhlbmpskgxmxosft",
     "vigplemkoni",
     "krdrlctodtmprpxwditvcps",
     "gqjwokkskrb",
     "bslxxpabivbvzkozzvdaykaatzrpe",
     "qwhzcwkchluwdnqjwhabroyyxbtsrsxqjnfpadi",
        "siqbezhkohmgbenbkikcxmvz",
        "ddmaireeouzcvffkcohxus",
        "kjzguljbwsxlrd",
        "gqzuqcljvcpmoqlnrxvzqwoyas",
        "vadguvpsubcwbfbaviedr",
        "nxnorutztxfnpvmukpwuraen",
        "imgvujjeygsiymdxp",
        "rdzkpk",
        "cuap",
        "qcojjumwp",
     "pyqzshwykhtyzdwzakjejqyxbganow",
     "cvxuskhcloxykcu",
     "ul",
     "axzscbjajazvbxffrydajapweci"],
    [[4, 4], [6, 17], [10, 17], [9, 18], [17, 22], [5, 23], [2, 5], [17, 21], [
        5, 17], [4, 8], [7, 17], [16, 19], [7, 12], [9, 20], [13, 23], [1, 5], [19, 19]]))
