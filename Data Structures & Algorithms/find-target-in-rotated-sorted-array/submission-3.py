from typing import List

class Solution:
    def search(self, nums: List[int],target:int)->int:
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            # left sorted
            elif nums[l] <= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted
            else: 
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
        
# time complexity: O(log n )
# space complexity: O(1)
nums = [3,4,5,6,1,2]
target = 1
print(Solution().search(nums, target))
nums = [3,5,6,0,1,2]
target = 4
print(Solution().search(nums, target))


            
            
            
            