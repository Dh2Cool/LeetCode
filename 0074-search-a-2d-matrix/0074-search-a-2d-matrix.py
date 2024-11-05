class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        top = 0
        bot = rows - 1
        while top <= bot:
            mid = (top+bot)//2
            if matrix[mid][0] > target:
                bot = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                break
        if not (top <= bot):
            return False
        mid = (top+bot)//2
        low, high = 0, cols-1
        while low<=high:
            mid1 = (low+high)//2
            if target > matrix[mid][mid1]:
                low = mid1 + 1
            elif target < matrix[mid][mid1]:
                high = mid1 -1
            else:
                return True
        return False
            