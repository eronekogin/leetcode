"""
https://leetcode.com/problems/rank-teams-by-votes/
"""


class Solution:
    def rankTeams(self, votes: list[str]) -> str:
        """
        Simply count the votes for each team on each level, then take
        advantage of the sort function in python to compare and sort for
        each level. Notice if the previous count are all tied, sort the
        teams in its char's alphabetical order then.
        """
        # Initialize counter.
        cnt = {
            c: [0] * len(votes[0]) + [c]
            for c in votes[0]
        }

        # Count teams.
        for v in votes:
            for i, c in enumerate(v):
                cnt[c][i] -= 1

        # Sort results.
        return ''.join(sorted(votes[0], key=lambda x: cnt[x]))


print(Solution().rankTeams(["ABC", "ACB", "ABC", "ACB", "ACB"]))
