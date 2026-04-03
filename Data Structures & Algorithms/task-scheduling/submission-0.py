class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}
        
        for task in tasks:
            counter[task] = 1 + counter.get(task,0)
        minHeap = [-cnt for cnt in counter.values()]
        heapq.heapify(minHeap)
        
        q = deque()
        time = 0
        while minHeap or q:
            time += 1

            if minHeap:
                cnt = heapq.heappop(minHeap) + 1
                if cnt:
                    q.append([cnt,time+n])
            if q and q[0][1] == time:
                heapq.heappush(minHeap,q.popleft()[0])
        return time


