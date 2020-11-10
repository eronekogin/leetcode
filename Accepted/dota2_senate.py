"""
https://leetcode.com/problems/dota2-senate/
"""


from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        """
        Simulate the voting process.
        """
        votes, remainParties, toBeBanned = deque(), [0, 0], [0, 0]

        # Scan the senate to initialize the lists.
        for c in senate:
            vote = int(c == 'R')
            votes.append(vote)
            remainParties[vote] += 1

        # Start voting until one party has no remainings.
        while all(remainParties):
            vote = votes.popleft()
            if toBeBanned[vote]:  # The current vote is banned.
                toBeBanned[vote] -= 1
                remainParties[vote] -= 1
            else:  # The senate could ban the other party and also vote again.
                toBeBanned[vote ^ 1] += 1
                votes.append(vote)

        return 'Radiant' if remainParties[1] else 'Dire'


print(Solution().predictPartyVictory('DDRRR'))
