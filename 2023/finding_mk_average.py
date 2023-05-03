"""
https://leetcode.com/problems/finding-mk-average/
"""


from heapq import heapify, heappush, heappop


class MKAverage:
    def _heap_init(self, l1: int, l2: int):
        h1 = [(0, i) for i in range(l1 - l2, l1)]
        h2 = [(0, i) for i in range(l1 - l2)]
        heapify(h1)
        heapify(h2)
        return (h1, h2)

    def _update(self, lh, rh, num: int):
        m = self.m
        score, t = 0, len(self.nums)
        if num > rh[0][0]:
            heappush(rh, (num, t))
            if self.nums[t - m] <= rh[0][0]:
                if rh[0][1] >= t - m:
                    score += rh[0][0]

                score -= self.nums[t - m]
                heappush(lh, (-rh[0][0], rh[0][1]))
                heappop(rh)
        else:
            heappush(lh, (-num, t))
            score += num
            if self.nums[t - m] >= rh[0][0]:
                heappush(rh, (-lh[0][0], lh[0][1]))
                score += heappop(lh)[0]
            else:
                score -= self.nums[t - m]

        # Lazy delete from heap
        while lh and lh[0][1] <= t - m:
            heappop(lh)

        while rh and rh[0][1] <= t - m:
            heappop(rh)

        return score

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.nums = [0] * m
        self.lh1, self.rh1 = self._heap_init(m, k)
        self.lh2, self.rh2 = self._heap_init(m, m - k)
        self.score = 0

    def addElement(self, num: int) -> None:
        t1 = self._update(self.lh1, self.rh1, num)
        t2 = self._update(self.lh2, self.rh2, num)
        self.nums.append(num)
        self.score += t2 - t1

    def calculateMKAverage(self) -> int:
        if len(self.nums) < (self.m << 1):
            return -1

        return self.score // (self.m - (self.k << 1))


mk = MKAverage(3, 1)
mk.addElement(3)
mk.addElement(1)
mk.addElement(10)
print(mk.calculateMKAverage())
