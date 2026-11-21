class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        column = len(matrix[0])

        l = 0
        r = row * column - 1

        while l <= r:
            m = (l + r) // 2
            row_idx, col_idx = m // column, m % column
            if target > matrix[row_idx][col_idx]:
                l = m + 1
            elif target < matrix[row_idx][col_idx]:
                r = m - 1
            else:   
                return True
        
        return False
