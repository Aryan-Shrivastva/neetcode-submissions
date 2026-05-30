# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        best = 0
        def diameter(root):
            nonlocal best
            if not root:
                return 0
            
            rightHeight = diameter(root.right)
            leftHeight = diameter(root.left)

            best = max(best, rightHeight+leftHeight +1)

            return max(leftHeight, rightHeight) +1

        
        diameter(root)
        return best -1