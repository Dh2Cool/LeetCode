class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        mid = 0
        res = nums[0]
        while l<=r:
            mid = (l+r)//2
            res = min(res, nums[mid])
            if nums[mid] >= nums[r]:
                l = mid + 1
            else:
                r = mid -1
        return res