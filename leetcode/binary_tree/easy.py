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


    # 226. Invert Binary Tree
    """
    Given the root of a binary tree, invert the tree, and return its root.
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Definition of inversion:
        1. Root always stays the same
        2. Left is now right and right is now left
        3. Every node from the first layer to the leaf is inverted.
        e.g. 
        1. root.left.left -> root.right.right
        2. root.left.right -> root.right.left

        Edge cases:
        1. If root only: return root (no need for inversion)
        2. If empty: return empty
        3. Can we create a new tree or do we have to do in place inversion and return the same tree?

        Pseudocode:
        Starting from root
        1. traverse recursively down the tree until we hit the layer before leaves
        2. invert the left and right nodes
        """
        if root is None:
            return root
        if root.left is None and root.right is None:
            return root
        elif root.left is None and root.right is not None:
            root.left = self.invertTree(root.right)
            root.right = None
        elif root.left is not None and root.right is None:
            root.right = self.invertTree(root.left)
            root.left = None
        else:
            temp_left_root = self.invertTree(root.right)
            root.right = self.invertTree(root.left)
            root.left = temp_left_root
        return root