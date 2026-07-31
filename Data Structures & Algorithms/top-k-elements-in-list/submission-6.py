class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = [[] for i in range(len(nums)+1)]

        counter = {}

        for n in nums:
            counter[n] = counter.get(n,0) + 1
        
        for n,count in counter.items():
            freq[count].append(n)
        
        res = []

        for i in range(len(freq)-1,-1,-1):

            while freq[i]:
                n = freq[i].pop()
                res.append(n)

                k -= 1

                if k == 0:
                    return res

# time complexity: O()
# space complexity: O()   