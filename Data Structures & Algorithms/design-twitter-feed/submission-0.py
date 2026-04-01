class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set) # {userId: a set of followee Ids}
        self.tweetMap = defaultdict(list) # {userId: a list of (time, tweetId)}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([-self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        # show all the followee Ids including the user id
        followeeIds = self.followMap[userId].copy()
        followeeIds.add(userId)

        for id in followeeIds:
            time_tweets = self.tweetMap.get(id, [])
            for tweet in time_tweets:
                heapq.heappush(maxHeap, tweet)
                if len(maxHeap) > 10:
                    heapq.heappop(maxHeap)
        res = []
        while maxHeap:
            res.append(heapq.heappop(maxHeap)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followeeIds = self.followMap[followerId] 
        if followeeIds and followeeId in followeeIds: 
            followeeIds.remove(followeeId)
        
