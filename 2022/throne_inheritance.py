"""
https://leetcode.com/problems/throne-inheritance/
"""


from collections import defaultdict


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.deadPeople: set[str] = set()
        self.children: defaultdict[str, list[str]] = defaultdict(list)
        self.parents: dict[str, str] = {}
        self.kingName = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)
        self.parents[childName] = parentName

    def death(self, name: str) -> None:
        self.deadPeople.add(name)

    def getInheritanceOrder(self) -> list[str]:
        def walk(root: str) -> list[str]:
            orders: list[str] = [root]
            for child in self.children[root]:
                orders.extend(walk(child))

            return orders

        orders: list[str] = walk(self.kingName)
        return [name for name in orders if name not in self.deadPeople]


t = ThroneInheritance('king')
t.birth('king', 'andy')
t.birth('king', 'bob')
t.birth('king', 'catherine')
t.birth('andy', 'matthew')
t.birth('bob', 'alex')
t.birth('bob', 'asha')
print(t.getInheritanceOrder())
t.death('bob')
print(t.getInheritanceOrder())
