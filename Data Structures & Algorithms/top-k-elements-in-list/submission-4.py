class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = []

        frequency = [[] for i in range(len(nums)+1)]
        counter = {}

        for n in nums:
            counter[n] = counter.get(n,0) + 1
        
        for n,cnt in counter.items():
            frequency[cnt].append(n)

        print(frequency)
        

        for i in range(len(frequency)-1,-1,-1):
            while frequency[i]:
                res.append(frequency[i].pop())
                print()
                k -= 1

                if  k == 0:
                    return res
        


# time complexity: O(n)
# space complexity: O(n)     