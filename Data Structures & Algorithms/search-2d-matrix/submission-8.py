class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            mid = (left + right)  // 2
            matrix_value = matrix[mid // len(matrix[0])][mid % len(matrix[0])]
            if target > matrix_value:
                left = left + 1
            elif target < matrix_value:
                right = right - 1
            else:
                return True
        return False
        