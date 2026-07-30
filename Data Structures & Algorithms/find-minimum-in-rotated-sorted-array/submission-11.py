class Solution:
    def findMin(self, nums: List[int]) -> int:

        

        res = float("inf")
        l,r = 0, len(nums)-1


        while l <= r:

            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                return res

            mid = (l + r) // 2

            # left sorted
            if nums[l] <= nums[mid]:
                res = min(res, nums[l])
                l = mid + 1
            # right soted 
            else:
                res = min(res, nums[mid])
                r = mid - 1

        return res

# time complexity: O(log n)
# space complexity: O(1)


