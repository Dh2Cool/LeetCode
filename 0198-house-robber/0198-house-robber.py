class Solution:
    
    def rob(self, nums: List[int]) -> int:
        odd = 0
        even = 0
        for i, j in enumerate(nums):
            if i%2 == 0:
                odd = max(odd+j, even)
            else:
                even = max(even+j, odd)
        return max(odd, even)