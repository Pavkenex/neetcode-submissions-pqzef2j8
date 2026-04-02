class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rowSize=len(matrix[0])
        targetRow=0
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                targetRow=i
                break

        l,r=0,rowSize-1

        while l<=r:
            mid = l+(r-l)//2
            if target == matrix[targetRow][mid]:
                return True
            elif matrix[targetRow][mid] > target:
                r=mid-1
            else:
                l=mid+1

         

        return False
        