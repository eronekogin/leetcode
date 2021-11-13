"""
https://leetcode.com/problems/smallest-sufficient-team/
"""


class Solution:
    def smallestSufficientTeam(
        self,
        reqSkills: list[str],
        people: list[list[str]]
    ) -> list[int]:
        skillMemo = {v: i for i, v in enumerate(reqSkills)}
        dp = {0: []}  # {required skills mask: sufficient team index list}
        for i, personSkills in enumerate(people):
            # Calculate the current person's skill mask.
            personSkillMask = 0
            for skill in personSkills:
                if skill in skillMemo:
                    personSkillMask |= 1 << skillMemo[skill]

            if personSkillMask == 0:  # None of his skills is needed.
                continue

            # When there is a team with only one person who already has all
            # of the needed skills that the current person has.
            if personSkillMask in dp and len(dp[personSkillMask]) == 1:
                continue

            for currSkillSet, team in list(dp.items()):
                nextSkillSet = currSkillSet | personSkillMask
                if nextSkillSet == currSkillSet:  # Already sufficient.
                    continue

                # When the nextSkillSet has no sufficient team or the
                # original sufficient team has more people than the current
                # team with the current person, update the team.
                if nextSkillSet not in dp or len(dp[nextSkillSet]) > len(team) + 1:
                    # Add this person to the team.
                    dp[nextSkillSet] = team + [i]

        # Return the sufficient team where all the skills are required.
        return dp[(1 << len(reqSkills)) - 1]


print(Solution().smallestSufficientTeam(
    ["java", "nodejs", "reactjs"],
    [["java"], ["nodejs"], ["nodejs", "reactjs"]]
))
