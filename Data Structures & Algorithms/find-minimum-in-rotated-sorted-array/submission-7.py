from typing import List

class Solution:
    def findMin(self, nums: List[int])->int:
  
        l,r = 0, len(nums)-1
        res = float("inf")
        
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = (l+r)//2
            res = min(res, nums[mid])
            # left sorted
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return res
# time complexity: O(log n)
# space complexity: O(1)
nums = [3,4,5,6,1,2]
print(Solution().findMin(nums))


nums = [4,5,0,1,2,3]
print(Solution().findMin(nums))

nums = [4,5,6,7]
print(Solution().findMin(nums))
        