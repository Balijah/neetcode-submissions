class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if matrix[0][0] == target:
            return True

        cols = (len(matrix[0]))
        rows = (len(matrix))


        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == target:
                    return True
        return False