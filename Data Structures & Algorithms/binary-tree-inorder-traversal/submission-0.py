# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #left root right

        def inorder(root, ans):
            if root is None:
                return 
            
            # ans = []

            inorder(root.left, ans)
            ans.append(root.val)
            inorder(root.right, ans)
        
        ans = []
        inorder(root, ans)
        return ans
        



