class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = {}

        freqList = [[] for _ in range(len(nums)+1)]
        print(freqList)

        for n in nums:
            counter[n] = counter.get(n,0) + 1
        

        for num,idx in counter.items():
            freqList[idx].append(num)
        
        res = []


        for i in range(len(freqList)-1,-1,-1):
            while freqList[i]:
                n = freqList[i].pop()
                k -= 1
                res.append(n)
                if k == 0:
                    return res

# time complexity: O(n)
# space complexity: O(n)
            