from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int):
        freq = [[] for i in range(len(nums)+1)]
        counter = {}
        res = []
        
        for n in nums:
            counter[n] = counter.get(n,0) + 1
        
        for num,cnt in counter.items():
            freq[cnt].append(num)
        
        for i in range(len(freq)-1,-1,-1):
            n = len(freq[i])
            for _ in range(n):
                res.append(freq[i].pop())
                k -= 1
                if k == 0:
                    # stop
                    return res
        return res   
# time complexity: O(n)
# space complexity: O(n)     
        