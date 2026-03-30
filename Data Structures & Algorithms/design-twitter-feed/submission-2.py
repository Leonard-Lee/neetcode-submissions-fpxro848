class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        followeeIds = self.followMap[userId].copy()
        followeeIds.add(userId)
        minHeap = []
        res = []
        for id in followeeIds:
            tweetList = self.tweetMap[id]
            if tweetList:
                idx = len(tweetList) - 1
                time, tweetId = tweetList[idx]
                minHeap.append([time, tweetId, idx, id])

        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            time, tweetId, idx, userId = heapq.heappop(minHeap)
            res.append(tweetId)
            idx -= 1
            if idx >= 0:
                time, tweetId = self.tweetMap[userId][idx]
                heapq.heappush(minHeap, [time, tweetId, idx, userId])

        return res
                
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
