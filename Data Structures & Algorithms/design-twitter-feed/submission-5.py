from collections import defaultdict
class Twitter:

    def __init__(self):
        self.idx = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.idx, tweetId])
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop(0)
        self.idx -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        self.follows[userId].add(userId)
        
        users = self.follows[userId]

        if len(self.follows[userId]) >= 10:
            maxHeap = []
            for user in users:
                if user in self.tweets:
                    index = len(self.tweets[user]) - 1
                    count, tweetId = self.tweets[user][index]
                    heapq.heappush(maxHeap, [-count, tweetId, user, index-1])
                    if len(maxHeap) > 10:
                        heapq.heappop(maxHeap)
            while maxHeap:
                cnt, tweetId, user, index = heapq.heappop(maxHeap)
                heapq.heappush(minHeap,[-cnt,tweetId,user,index])
        else:    
            for user in users:
                if user in self.tweets:
                    index = len(self.tweets[user])-1
                    count, tweetId = self.tweets[user][index]
                    heapq.heappush(minHeap, [count,tweetId,user,index-1])
        ans = []
        while minHeap and len(ans)<10:
            cnt, tweetId, user, index = heapq.heappop(minHeap)
            ans.append(tweetId)
            if index >= 0:
                cnt, tweetId = self.tweets[user][index]
                heapq.heappush(minHeap, [cnt, tweetId, user, index-1])
            
        return ans
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        