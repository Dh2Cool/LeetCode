# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import lru_cache
class Solution:
    @lru_cache()
    def rob(self, root: Optional[TreeNode]) -> int:
        if(root == None):
            return 0
        dontrob = self.rob(root.left) + self.rob(root.right)
        robb = root.val
        if(root.left):
            robb += self.rob(root.left.left) + self.rob(root.left.right)
        if(root.right):
            robb += self.rob(root.right.left) + self.rob(root.right.right)
        return max(dontrob, robb)
        