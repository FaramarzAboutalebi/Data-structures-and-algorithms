class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = [[] for i in range(len(nums)+1)]
        counter = {}
        res = []
        for n in nums:
            counter[n] = counter.get(n,0) + 1
        
        for num,cnt in counter.items():
            freq[cnt].append(num)
        
        for i in range(len(freq)-1,-1,-1):
            while freq[i]:
                n = freq[i].pop()
                res.append(n)
                k -= 1
                if k == 0:
                    return res
        return res
        