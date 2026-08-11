class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n,m = len(matrix),len(matrix[0])

        i = 0
        j = n*m-1
        while i <= j:

            mid = (i+j)//2
            val = matrix[mid//m][mid%m]
            if val==target:
                return True
            elif val>target:
                j = mid-1
            else:
                i = mid+1
        return False
            