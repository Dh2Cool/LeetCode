class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        anslower = 0
        nums.sort()
        while l<r:
            sum = nums[l] + nums[r]
            if sum < lower:
                anslower += r - l
                l += 1
            else:
                r -= 1
        ansupper = 0
        l, r = 0, n-1
        while l < r:
            sum = nums[l] + nums[r]
            if sum < upper+1:
                ansupper += r - l
                l += 1
            else:
                r -= 1
        return ansupper - anslower
