"""
https://leetcode.com/problems/tweet-counts-per-frequency/
"""


from collections import defaultdict


class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(
        self,
        freq: str,
        tweetName: str,
        startTime: int,
        endTime: int
    ) -> list[int]:
        interval = 60
        if freq == 'hour':
            interval *= 60
        elif freq == 'day':
            interval *= 24 * 60

        totalChunks = (endTime - startTime) // interval
        rslt = [0] * (totalChunks + 1)
        for time in self.tweets[tweetName]:
            if startTime <= time <= endTime:
                i = (time - startTime) // interval
                rslt[i] += 1

        return rslt
