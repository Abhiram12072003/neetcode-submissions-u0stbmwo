from collections import defaultdict
class Twitter:

    def __init__(self):
        self.idx = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        print(self.tweets, self.follows)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.idx, tweetId])
        self.idx += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        lis = []
        users = self.follows[userId]

        for user in users:
            for twitterId in self.tweets[user]:
                lis.append([-twitterId[0], twitterId[1]])
        if userId not in users:
            for twitterId in self.tweets[userId]:
                lis.append([-twitterId[0], twitterId[1]])
            
        heapq.heapify(lis)
        
        cnt = 10
        ans = []
        for i in range(cnt):
            if not lis:
                break
            ans.append(heapq.heappop(lis)[1])
        
        return ans
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            if followeeId in self.follows[followerId]:
                self.follows[followerId].remove(followeeId)
        