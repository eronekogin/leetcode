"""
https://leetcode.com/problems/statistics-from-a-large-sample/
"""


class Solution:
    def sampleStats(self, count: list[int]) -> list[float]:
        totalCnt = totalSum = maxCnt = mode = 0
        minNum, maxNum = 256, -1
        for num, cnt in enumerate(count):
            if cnt:
                totalCnt += cnt
                totalSum += num * cnt
                minNum = min(minNum, num)
                maxNum = max(maxNum, num)
                if cnt > maxCnt:
                    maxCnt, mode = cnt, num

        mean = totalSum / totalCnt

        # Calculate median.
        maxCnt = totalCnt / 2
        currCnt = median = 0
        for num, cnt in enumerate(count):
            if cnt:
                if currCnt + cnt > maxCnt:
                    if not median:
                        median = num
                    else:
                        median = (median + num) / 2

                    break
                elif currCnt + cnt == maxCnt:
                    if totalCnt & 1:
                        median = float(num)
                        break
                    else:
                        median = num

                currCnt += cnt

        return [float(minNum), float(maxNum), mean, median, float(mode)]


print(Solution().sampleStats(
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
     0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
))
