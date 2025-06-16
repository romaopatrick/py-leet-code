# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right
        
    
        
    
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.check_depth(root)
    
    def check_depth(self, node: TreeNode) -> int:
        if node is None:
            return 0
        
        left, right = 0, 0
        left += self.check_depth(node.left)
        right += self.check_depth(node.right)
        
        return max(left, right) + 1
        