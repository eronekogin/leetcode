"""
https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/
"""


class Solution:
    def peopleIndexes(self, favoriteCompanies: list[list[str]]) -> list[int]:
        sortedIndexes = sorted(
            [(l, i) for i, l in enumerate(favoriteCompanies)],
            key=lambda x: -len(x[0])
        )

        rslt: list[int] = []
        for l, i in sortedIndexes:
            if not rslt:
                rslt.append(i)
                continue

            isSubset = False
            for j in rslt:
                if set(l) < set(favoriteCompanies[j]):
                    isSubset = True
                    break

            if not isSubset:
                rslt.append(i)

        return sorted(rslt)
