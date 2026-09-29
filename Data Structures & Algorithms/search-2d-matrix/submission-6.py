class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        cols = (len(matrix[0]))
        rows = (len(matrix))


        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == target:
                    return True
        return False