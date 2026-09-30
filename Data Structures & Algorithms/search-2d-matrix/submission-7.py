class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])
        number_of_elements = rows * cols

        left = 0
        right = number_of_elements - 1

        while left <= right:
            mid = (left + right)  // 2
            matrix_value = matrix[mid // cols][mid % cols]
            if target > matrix_value:
                left = left + 1
            elif target < matrix_value:
                right = right - 1
            else:
                return True
        return False
        