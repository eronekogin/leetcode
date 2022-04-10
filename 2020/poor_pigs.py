"""
https://leetcode.com/problems/poor-pigs/
"""


class Solution:
    def poorPigs(
            self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        """
        1. Suppose we have only 2 pigs, 15 minutes to die and 60 minutes to
            test. And we have our buckets listed as below:

            1  2  3  4  5
            6  7  8  9 10
            11 12 13 14 15
            16 17 18 19 20
            21 22 23 24 25

        2. We have 1 pig drink for each row and 1 pig drink for each column,
            then with the time limit each pig could drink either 4 rows or
            4 columns.

        3. If the first pig dies on the third test while the second pig does
            not die at all, we could make sure the poison is on the fifth
            column, which will be item #15.

        4. If we have three pigs, we could make sure of 5 * 5 * 5 = 5 ^ pigs.
        """
        pigs, size = 0, minutesToTest // minutesToDie + 1
        while size ** pigs < buckets:
            pigs += 1

        return pigs
