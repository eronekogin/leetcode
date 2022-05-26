"""
https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/
"""


from collections import deque


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        nextChars = {
            'a': 'bc',
            'b': 'ac',
            'c': 'ab'
        }
        queue = deque(list('abc'))
        while len(queue[0]) < n:
            c = queue.popleft()
            for nextChar in nextChars[c[-1]]:
                queue.append(c + nextChar)

        if len(queue) < k:
            return ''

        return queue[k - 1]


print(Solution().getHappyString(3, 9))
