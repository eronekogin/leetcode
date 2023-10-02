"""
https://leetcode.com/problems/find-array-given-subset-sums/
"""


from collections import Counter


class Solution:
    def recoverArray(self, n: int, sums: list[int]) -> list[int]:
        def recover(sums: list[int]) -> list[int]:
            if len(sums) < 2:  # Original list is empty.
                return []

            cnt = Counter(sums)
            splitA: list[int] = []
            splitB: list[int] = []
            needsMoreSplit = False

            x = sums[-1] - sums[-2]  # x or -x is the number from the original list.
            for a in sums:
                b = a - x
                if cnt[b] > 0 and cnt[a] > 0:  # Found a sum composed by x, split it.
                    cnt[a] -= 1
                    cnt[b] -= 1
                    splitA.append(a)
                    splitB.append(b)
                    if b == 0:
                        needsMoreSplit = True
            
            if needsMoreSplit:
                return [x] + recover(splitB)

            return [-x] + recover(splitA)

        return recover(sorted(sums))


print(Solution().recoverArray(3, [-3,-2,-1,0,0,1,2,3]))