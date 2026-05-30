# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #binary search, like if p and q exist on left, return curr becomes the left root 
        #else if p,q greater than curr, curr becommes right root, else we return the curr root
        curr = root

        while curr is not None:

            if p.val>curr.val and q.val>curr.val:
                curr = curr.right
            elif p.val<curr.val and q.val<curr.val:
                curr = curr.left
            else:
                return curr