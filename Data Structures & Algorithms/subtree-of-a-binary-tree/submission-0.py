# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def same(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            
            if p.val!=q.val:
                return False

            left = same(p.left, q.left)
            right = same(p.right, q.right)

            return left and right
        

        def has_subtree(root):
            if root is None:
                return False
            
            if same(root, subRoot):
                return True
            
            left = has_subtree(root.left)
            right = has_subtree(root.right)

            return left or right
        
        return has_subtree(root)