"""
https://leetcode.com/problems/find-duplicate-file-in-system/
"""


from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        """
        When file contents are short, just use the simple solution below.

        1. When handling a real file system, if each directory contains less
            files, we could use DFS to search those files instead of BFS to
            reduce memory usage.
        2. When the file is too large, we could take advantage of file meta
            data like file size. Once we found two files containing the same
            file size, we could compare their md5 checksum value to see if
            they are identical.
        3. When the file could only be read 1kb each time, we should compare
            the file having the same size and md5 checksum chunk by chunk.
        4. The most time consuming part is the md5 checksum part when performed
            against the whole file contents. Instead we could apply it to each
            small chunk to accelarate the process.
        5. The false positive caused by comparing the whole file size and file
            chunk could be solved by comparing each small chunk instead.
        """
        memo = {}  # {file contents: list of file path}
        for p in paths:
            items = p.split()
            root = items[0]
            for i in range(1, len(items)):
                fn, contents = items[i].split('(')
                memo[contents] = memo.get(
                    contents, []) + ['/'.join([root, fn])]

        return [fns for fns in memo.values() if len(fns) > 1]


print(Solution().findDuplicate(
    [
        "root/a 1.txt(abcd) 2.txt(efsfgh)",
        "root/c 3.txt(abdfcd)",
        "root/c/d 4.txt(efggdfh)"]))
