"""
https://leetcode.com/problems/finding-pairs-with-a-certain-sum/
"""


from collections import Counter


class FindSumPairs:

    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.cnt = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.cnt[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.cnt[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        return sum(self.cnt[tot - x] for x in self.nums1)


f = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])
f.count(7)
f.add(3, 2)
f.count(8)
f.count(4)
f.add(0, 1)
f.add(1, 1)
f.count(7)
