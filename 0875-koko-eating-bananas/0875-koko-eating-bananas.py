class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = 1
        while l<=r:
            mid = (l+r)//2
            totaltime = 0
            for p in piles:
                totaltime += math.ceil(p/mid)
            if totaltime <= h:
                ans = mid
                r = mid -1
            else:
                l = mid + 1
        return ans