class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(i,temp):
            if i == len(nums):
                res.append(temp.copy())
                return 
            temp.append(nums[i])
            dfs(i+1,temp)
            temp.pop()
            dfs(i+1,temp)
        


        dfs(0,[])
        return res