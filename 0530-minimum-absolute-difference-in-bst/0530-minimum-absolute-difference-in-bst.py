# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            if self.prev is not None:
                self.min_dist = min(self.min_dist, node.val - self.prev)
            self.prev = node.val
            inOrder(node.right)
            
        self.min_dist = math.inf
        self.prev = None
        inOrder(root)
        return self.min_dist