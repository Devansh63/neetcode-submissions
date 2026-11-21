class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        column = len(matrix[0])

        start = 0
        stop = row - 1

        while start <=stop:
            tempR = (start+stop) // 2
            if target > matrix[tempR][-1]:
                start = tempR+1
            elif target < matrix[tempR][0]:
                stop = tempR -1
            else:
                break
            
        if not (start <= stop):
            return False
        tempR = (start+stop) //2
        left,right = 0, column -1
        while left <= right:
            middle = (left+right)//2
            if target > matrix[tempR][middle]:
                left = middle+1
            elif target < matrix[tempR][middle]:
                right = middle -1
            else:
                return True
        return False
