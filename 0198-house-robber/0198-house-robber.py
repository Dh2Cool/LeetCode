from functools import lru_cache
class Solution:
    
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        return self.robber(len(nums)-1)
    @lru_cache()
    def robber(self, n) -> int:
        if n < 0:
            return 0
        
        return max(self.robber(n-2)+self.nums[n], self.robber(n-1))