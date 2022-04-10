"""
https://leetcode.com/problems/iterator-for-combination/
"""


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.pointers = [i for i in range(combinationLength)]
        self.text = characters
        self.maxIndex = len(characters)

    def next(self) -> str:
        rslt = None
        if self.hasNext():
            rslt = ''.join(self.text[i] for i in self.pointers)

            # Try to find the next combination of the pointer
            # by adding 1 to the last pointer.
            i, n = 1, len(self.pointers)
            while i <= n and self.pointers[n - i] + i == self.maxIndex:
                i += 1

            if i == n + 1:
                # Simply set the last pointer to the max index to
                # indicate that all the combinations are exhuasted now.
                self.pointers[-1] = self.maxIndex
            else:  # We still have more combination coming.
                nextStart = n - i
                nextVal = self.pointers[nextStart] + 1
                self.pointers[nextStart:] = [
                    v for v in range(nextVal, nextVal + i)]

        return rslt

    def hasNext(self) -> bool:
        return self.pointers[-1] < self.maxIndex


c = CombinationIterator('abcde', 3)
while c.hasNext():
    print(c.next())
