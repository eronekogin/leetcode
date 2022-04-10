"""
https://leetcode.com/problems/get-watched-videos-by-your-friends/
"""


from collections import Counter


class Solution:
    def watchedVideosByFriends(
        self,
        watchedVideos: list[list[str]],
        friends: list[list[int]],
        id: int,
        level: int
    ) -> list[str]:
        def get_friends_at_level(id: int, level: int) -> list[int]:
            visited = {id}
            currFriends = [id]
            for _ in range(level):
                newFriends = []
                for friend in currFriends:
                    for newFriend in friends[friend]:
                        if newFriend not in visited:
                            visited.add(newFriend)
                            newFriends.append(newFriend)

                currFriends = newFriends

            return currFriends

        currFriends = get_friends_at_level(id, level)
        cnt = Counter(
            video
            for friend in currFriends
            for video in watchedVideos[friend]
        )

        return [
            key
            for key, _ in sorted(cnt.items(), key=lambda x: (x[1], x[0]))
        ]


print(Solution().watchedVideosByFriends([["A", "B"], ["C"], ["B", "C"], ["D"]],
                                        [[1, 2], [0, 3], [0, 3], [1, 2]],
                                        0,
                                        2))
