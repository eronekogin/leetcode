"""
https://leetcode.com/problems/reaching-points/
"""


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        """
        1. Since at each point we could only go two direction, either
            (x + y, y) or (x, x + y), we could take it as a tree with root as
            (sx, sy) and check if node (tx, ty) is in the current tree.
        2. If we search the path from the root, we will get TLE.
        3. Then we could try to search from the target node to the root by
            reducing the tx or ty evetually to sx or sy.
        4. The reducing process goes like:
            4.1 If our current node is (tx, ty), in order to reach it, we
                either come from (tx - ty, ty) when tx > ty or (tx, ty - tx)
                when tx < ty.
            4.2 If tx > ty, tx % ty, ty % tx gives us tx - k * ty, ty.
            4.3 If ty > tx, tx % ty, ty % tx gives us tx, ty - k * tx.
            4.4 Evetually we will reach a point when tx <= sx or ty <= sy.
        5. If sx == tx, then check if ty = sy + k * tx.
        6. If sy == ty, then check if tx = sx + k * ty.
        7. For other cases such as if sx > tx or sy > ty, it means we could not
            reach the root node, which indicate the target node is not in
            the tree.
        """
        while sx < tx and sy < ty:
            tx, ty = tx % ty, ty % tx

        return sx == tx and sy <= ty and (ty - sy) % sx == 0 or \
            sy == ty and sx <= tx and (tx - sx) % sy == 0


print(Solution().reachingPoints(3, 3, 12, 9))
