class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        R = len(matrix)
        C = len(matrix[0])
        
        row = 0
        col = C-1

        while row<R and col>=0:
            if matrix[row][col]>target:
                col-=1
            elif matrix[row][col]<target:
                row+=1
            else:
                return True
        
        return False