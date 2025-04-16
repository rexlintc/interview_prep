from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # 104. Maximum Depth of Binary Tree
    """
    Given the root of a binary tree, return its maximum depth.

    A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

    Input: root = [3,9,20,null,null,15,7]
    Output: 3
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(root):
            if root is None:
                return 0
            else:
                return 1 + max(traverse(root.left), traverse(root.right))
        if root is None:
            return 0
        left_depth, right_depth = 1, 1
        if root.left:
            left_depth += traverse(root.left)
        if root.right:
            right_depth += traverse(root.right)
        return max(left_depth, right_depth)
    
    # 100. Same Tree
    """
    Given the roots of two binary trees p and q, write a function to check if they are the same or not.

    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
    Input: p = [1,2,3], q = [1,2,3]
Output: true
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)