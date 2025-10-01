"""
https://leetcode.com/problems/shortest-string-that-contains-three-strings/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_string(self, a: str, b: str, c: str) -> str:
        """
        minimum string
        """
        def concat(x: str, y: str) -> str:
            if x in y:
                return y

            if y in x:
                return x

            i = x.find(y[0])
            while i != -1:
                if y.startswith(x[i:]):
                    return x + y[len(x) - i:]

                i = x.find(y[0], i + 1)

            return x + y

        candidates = sorted([
            concat(concat(a, b), c),
            concat(concat(a, c), b),
            concat(concat(b, a), c),
            concat(concat(b, c), a),
            concat(concat(c, a), b),
            concat(concat(c, b), a)
        ], key=lambda x: (len(x), x))

        return candidates[0]


print(Solution().minimum_string('cab', 'a', 'b'))
