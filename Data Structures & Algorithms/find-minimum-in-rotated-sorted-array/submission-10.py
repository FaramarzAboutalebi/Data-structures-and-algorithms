class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        l,r = 0, len(nums)-1

        res = float("inf")

        while l <= r:

            mid = (l+r) // 2

            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                return res

            # left side sorted
            if nums[l] <= nums[mid]:
                res = min(res, nums[l])
                l = mid + 1

            # rigth side sorted 
            else:
                res = min(res, nums[mid])
                r = mid - 1

        return res

# time complexity: O(log n)
# space complexity: O(1)