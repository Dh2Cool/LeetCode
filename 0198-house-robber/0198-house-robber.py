class Solution:
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        res = [0 for x in range(len(nums))]
        res[0] = nums[0]
        res[1] = nums[1]
        for i in range(len(nums)):
            if i+2 < len(nums):
                res[i+2] = max(res[i+2],res[i]+nums[i+2])
            if i+3 < len(nums):
                res[i+3] = max(res[i+3],res[i]+nums[i+3])
        print(res)
        return max(res[-1],res[-2])
            