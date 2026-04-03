import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):  # O(1) time, O(1) space
        self.time = 0  # O(1): global timestamp counter
        self.userTweets = defaultdict(list)  # O(1): maps userId -> List of (timestamp, tweetId)
        self.following = defaultdict(set)  # O(1): maps userId -> set of followees

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append((self.time, tweetId))  # O(1) time, O(1) space per tweet
        self.time -= 1  # Decrease time to simulate max-heap with min-heap → O(1)

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []  # O(1) time, O(1) space

        self.following[userId].add(userId)  # O(1): ensure user sees their own tweets

        # Add latest tweets of each followed user into the heap
        for followeeId in self.following[userId]:  # O(f), f = number of followees
            tweets = self.userTweets[followeeId]  # O(1)
            for i in range(len(tweets) - 1, max(-1, len(tweets) - 11), -1):  # O(10) per user max
                heapq.heappush(heap, tweets[i])  # O(log k), k ≤ total tweets considered

        # Extract top 10 most recent tweets
        res = []
        while heap and len(res) < 10:  # O(10)
            _, tweetId = heapq.heappop(heap)  # O(log k)
            res.append(tweetId)  # O(1)

        return res  # O(1)

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:  # O(1)
            self.following[followerId].add(followeeId)  # O(1) time, O(1) space

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:  # O(1)
            self.following[followerId].remove(followeeId)  # O(1)
