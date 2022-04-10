"""
https://leetcode.com/problems/3sum-with-multiplicity/
"""


from collections import Counter


class Solution:
    def threeSumMulti(self, arr: list[int], target: int) -> int:
        cnt = Counter(arr)
        uniqueNums = sorted(cnt)
        rslt = 0

        for i, x in enumerate(uniqueNums):
            remain = target - x
            j, k = i, len(uniqueNums) - 1
            while j <= k:
                y, z = uniqueNums[j], uniqueNums[k]
                if y + z < remain:  # Too small.
                    j += 1
                elif y + z > remain:  # Too large.
                    k -= 1
                else:  # Equal.
                    if i < j < k:
                        rslt += cnt[x] * cnt[y] * cnt[z]
                    elif i == j < k:
                        rslt += cnt[x] * (cnt[x] - 1) * cnt[z] // 2
                    elif i < j == k:
                        rslt += cnt[x] * cnt[y] * (cnt[y] - 1) // 2
                    else:  # i == j == k, choose 3 from cnt[x]
                        rslt += cnt[x] * (cnt[x] - 1) * (cnt[x] - 2) // 6

                    j += 1
                    k -= 1

        return rslt % (10 ** 9 + 7)
