class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        l = 0
        r = ROWS * COLS - 1
        
        while l<=r:
            middle = ((r-l)//2) + l
            row = middle // COLS
            col = middle % COLS
            if target > matrix[row][col]:
                l = middle + 1
            elif target < matrix[row][col]:
                r = middle - 1
            else:
                return True
        
        return False




