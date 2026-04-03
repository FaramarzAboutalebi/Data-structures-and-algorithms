from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int)->List[int]:
        
        counter = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            counter[n] = counter.get(n,0) + 1
        
        for n,cnt in counter.items():
            freq[cnt].append(n)
        
        res = []
        
        for i in range(len(freq)-1,-1,-1):
            while freq[i]:
                num = freq[i].pop() # O(1)
                res.append(num)
                k -= 1
                
                if k == 0:
                    return res
        return res
            
# time complexity: O(n)
# space complexity: O(n)
nums = [1,2,2,3,3,3]
k = 2          
print(Solution().topKFrequent(nums, k))    
nums = [7,7]
k = 1
print(Solution().topKFrequent(nums, k))
            
            
        