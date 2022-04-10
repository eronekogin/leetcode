"""
https://leetcode.com/problems/number-of-music-playlists/
"""


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        """
        1. Suppose dp[i][j] stands for the number of playlist of length i for
            j unique songs, then consider the last song added to this playlist:
            1.1 If the last song is not played before, we could choose it from
                the remaining n - j + 1 songs:
                dp[i][j] = dp[i - 1][j - 1] * (n - j + 1)
            1.2 If the last song is played before, we could choose it from
                the songs before the previous k songs:
                dp[i][j] = dp[i - 1][j] * max(j - k, 0) 
        """
        # Initialize when goal == 0, notice zero song fits in zero length
        # play list, so dp[0][0] = 1.
        currItems = [1] + [0] * n

        # Calculate each level until level == goal.
        for i in range(1, goal + 1):
            nextItems = [0] * (n + 1)

            # j has to be less or equal than i in order for each song to be
            # played once, also j has to be less or equal than n as we only
            # have n maximum unique songs.
            for j in range(1, 1 + min(i, n)):
                nextItems[j] = currItems[j - 1] * (n - j + 1)
                nextItems[j] += currItems[j] * max(j - k, 0)

            currItems = nextItems

        return currItems[-1] % (10 ** 9 + 7)


print(Solution().numMusicPlaylists(3, 3, 1))
