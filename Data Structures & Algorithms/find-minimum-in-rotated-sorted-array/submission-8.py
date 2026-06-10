class Solution:
    def findMin(self, nums: List[int]) -> int:


        left, right = 0, len(nums) - 1

        res = float("inf")

        while left <= right:

            if nums[left] <= nums[right]:
                res = min(res, nums[left])
                break

            mid = (left + right) // 2

            
            res = min(res, nums[mid])

            # left sorted
            if nums[left] <= nums[mid]:
                res = min(res, nums[left])  
                left = mid + 1  
            # right sorted
            else:
                right = mid - 1

        return res

# time complexity: O(log n)
# space complexity: O(1)


        