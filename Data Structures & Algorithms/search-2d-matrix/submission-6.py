class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r=0, len(matrix)-1
        mid = 0,0
        while l<=r:
            mid = (l+r)//2
            if matrix[mid][-1] < target:
                l = mid + 1
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                break
            
        if not l<=r:
            return False
        
        targetRow=(r+l)//2

        l,r =0, len(matrix[targetRow])-1

        while l<=r:
            mid = (l+r)//2
            if target == matrix[targetRow][mid]:
                return True
            elif matrix[targetRow][mid] > target:
                r=mid-1
            else:
                l=mid+1

        return False

