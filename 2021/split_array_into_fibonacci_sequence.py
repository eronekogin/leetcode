"""
https://leetcode.com/problems/split-array-into-fibonacci-sequence/
"""


class Solution:
    def splitIntoFibonacci(self, S: str) -> list[int]:
        """
        1. Notice that the numbers in the result set is less than 2^31 - 1,
            which means the length of each number should be less than 10.
        2. Another thing is is that the sequence of F is only determined by
            the first two elements, so we could enumerate all the cases of
            the first two elements, then check if the remaining numbers could
            form the sequence.
        """
        N, MAX_NUM = len(S), (1 << 31) - 1
        for i1 in range(min(10, N)):
            n1 = S[:i1 + 1]
            if n1 != '0' and n1.startswith('0'):
                break

            n1 = int(n1)
            for i2 in range(i1 + 1, min(i1 + 10, N)):
                n2 = S[i1 + 1: i2 + 1]
                if n2 != '0' and n2.startswith('0'):
                    break

                n2 = int(n2)
                rslt = [n1, n2]
                i3 = i2 + 1
                while i3 < N:
                    n3 = rslt[-1] + rslt[-2]
                    if n3 <= MAX_NUM and S[i3:].startswith(str(n3)):
                        i3 += len(str(n3))
                        rslt.append(n3)
                    else:
                        break
                else:  # Not break in the middle.
                    if len(rslt) >= 3:
                        return rslt

        return []
