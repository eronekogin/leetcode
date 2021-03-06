"""
https://leetcode.com/problems/design-twitter/
"""


from typing import List
from collections import defaultdict, deque
from itertools import count, islice
from heapq import merge


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timer = count(0, -1)
        self.tweets = defaultdict(deque)  # userId: Deque[(timer, tweetId)]
        self.followees = defaultdict(set)  # followerId: List[followeeId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId].appendleft((next(self.timer), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. 
        Each item in the news feed must be posted by users 
        who the user followed or by the user herself.
        Tweets must be ordered from most recent to least recent.
        """
        # Get all the tweets generated by this user and the people he follows.
        tweets = [self.tweets[u] for u in self.followees[userId] | {userId}]

        # Use heap sort to generate an iterator that fetch the smallest
        # item among those tweet queues.
        tweets = merge(*tweets)

        # Get the first 10 smallest tweets, which then will be our most
        # recent tweets this user and his followees has created.
        return [tweetId for _, tweetId in islice(tweets, 10)]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. 
        If the operation is invalid, it should be a no-op.
        """
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. 
        If the operation is invalid, it should be a no-op.
        """
        self.followees[followerId].discard(followeeId)
