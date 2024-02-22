"""
https://leetcode.com/problems/find-substring-with-given-hash-value/description/
"""


class Solution:
    """
    Solution
    """

    def sub_str_hash(self, s: str, power: int, modulo: int, k: int, hash_value: int) -> str:
        """
        hash(s, p, m) = (v1 * p^0 + v2 * p^1 + ... + vn-1 * p^(n - 1)) % m

        Consider s = 'abc', curr = 0

        Iteration#1: curr = c + curr * p -> curr = c

        Iteration#2: curr = b + curr * p -> curr = b + c * p

        Iteration#3: curr = a + curr * p -> curr = a + (b + c * p) * p = a + b * p + c * p ^ 2

        Which means curr = hash(abc, p, m)
        """
        def val(c: str):
            return ord(c) - offset + 1

        offset = ord('a')
        rslt = n = len(s)
        pk = pow(power, k, modulo)
        curr = 0

        for i in range(n - 1, -1, -1):
            curr = (curr * power + val(s[i])) % modulo

            if i + k < n:
                curr = (curr - val(s[i + k]) * pk) % modulo

            if curr == hash_value:
                rslt = i

        return s[rslt: rslt + k]


print(Solution().sub_str_hash('xmmhdakfursinye', 96, 45, 15, 21))
