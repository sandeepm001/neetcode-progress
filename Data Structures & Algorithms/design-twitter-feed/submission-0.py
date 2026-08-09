class Twitter:
    def __init__(self):
        self.tweet = defaultdict(list)
        self.following = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append((-self.time,tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        import heapq
        heap = []

        users = self.following[userId] + [userId]

        for userid in users:
            for item in self.tweet[userid]:
                heapq.heappush(heap,item)
        i = 0
        res = []
        while heap and i<10:
            val = heapq.heappop(heap)
            res.append(val[1])
            i += 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId not in self.following[followerId]:
            self.following[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        

        
