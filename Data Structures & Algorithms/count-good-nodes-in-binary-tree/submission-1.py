# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count = 0

        def dfs(root, best):
            nonlocal count

            if root is None:
                return

            if root.val>=best:
                count+=1
            
            best = max(best, root.val)

            dfs(root.left, best)
            dfs(root.right, best)
        
        INF = 10**20
        dfs(root, -INF)
        return count