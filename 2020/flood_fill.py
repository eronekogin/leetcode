"""
https://leetcode.com/problems/flood-fill/
"""


from typing import List


class Solution:
    def floodFill(
            self, image: List[List[int]],
            sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image or not image[0]:
            return image

        R, C = len(image), len(image[0])
        newImage = [[num for num in row] for row in image]
        oldColor = image[sr][sc]
        if oldColor == newColor:  # Already filled with new color.
            return image

        def fill(r: int, c: int):
            if newImage[r][c] == oldColor:
                newImage[r][c] = newColor
                if r > 0:
                    fill(r - 1, c)

                if r < R - 1:
                    fill(r + 1, c)

                if c > 0:
                    fill(r, c - 1)

                if c < C - 1:
                    fill(r, c + 1)

        fill(sr, sc)
        return newImage
