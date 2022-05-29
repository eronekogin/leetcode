"""
https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/
"""


class Solution:
    def displayTable(self, orders: list[list[str]]) -> list[list[str]]:
        foods = sorted({food for _, _, food in orders})
        foodMemo = {food: i + 1 for i, food in enumerate(foods)}
        rslt = [
            ['Table', *foods]
        ]
        for _, table, food in sorted(orders, key=lambda x: int(x[1])):
            if table != rslt[-1][0]:  # new table.
                rslt.append([table] + [0] * len(foods))

            rslt[-1][foodMemo[food]] += 1

        # Convert number to string.
        for r in range(1, len(rslt)):
            for c in range(1, len(rslt[0])):
                rslt[r][c] = str(rslt[r][c])

        return rslt
