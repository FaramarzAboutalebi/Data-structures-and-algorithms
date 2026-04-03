from typing import List

class Solution:
    def threeSum(self, nums: List[int])->List[int]:
        
        nums.sort() # O(n log n)
        
        res = []
        
        for i in range(len(nums)-2):

            if nums[i] > 0:
            
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums)-1
            
            while l < r:
                
                total = nums[i] + nums[l] + nums[r]
            
                
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                    
                elif total > 0:
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif total < 0:
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res
                    
# time complexity: O(n)
# space complexity: O(k), k <= n-2
nums = [-1,0,1,2,-1,-4]  

print(Solution().threeSum(nums) == [[-1,-1,2],[-1,0,1]])
nums = [0,1,1]
print(Solution().threeSum(nums) == [])
            

        
        