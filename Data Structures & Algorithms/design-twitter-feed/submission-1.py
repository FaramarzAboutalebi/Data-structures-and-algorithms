class Twitter:

    def __init__(self):
        self.time = 0
        self.userTweets = defaultdict(list)
        self.following = defaultdict(set)        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append([self.time,tweetId])
        self.time -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        self.following[userId].add(userId)
        minHeap = []

        for followeedId in self.following[userId]:
            tweets = self.userTweets[followeedId]
            for i in range(len(tweets) -1 , max(len(tweets)-11,-1), -1):
                heapq.heappush(minHeap,tweets[i])

        res = []
        while minHeap and len(res) < 10:
            time,tweetId = heapq.heappop(minHeap)
            res.append(tweetId)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
