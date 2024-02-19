class RecentCounter:

    def __init__(self):
        self.recent = 0
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.recent +=1
        self.queue.append(t)
        while self.queue[0] < t-3000:
            self.queue.popleft()
            self.recent-=1
    
        return self.recent
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)