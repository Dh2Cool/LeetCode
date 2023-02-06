class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        j=0
        k=n
        a=[]
        for i in range(0, n):
            a.append(nums[j])
            a.append(nums[k])
            j+=1
            k+=1
        return a