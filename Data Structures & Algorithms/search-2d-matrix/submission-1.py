class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        R = len(matrix)
        C = len(matrix[0])
        ans = []
        for row in matrix:
            for num in row:
                ans.append(num)
        n = len(ans)
        left = 0
        right = n-1

        if target not in ans:
            return False

        # while left<right:
        #     mid = (left+right)//2

        #     if ans[mid]==target:
        #         return True
        #     elif ans[mid]>target:
        #         left= mid+1
        #     else:
        #         right = mid

        if target in ans:
            return True