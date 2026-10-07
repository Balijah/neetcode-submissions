class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bot = rows - 1

        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                left = 0
                right = cols - 1

                while left <= right:
                    mid_element = (right + left) // 2
                    if target > matrix[mid][mid_element]:
                        left = mid_element + 1
                    elif target < matrix[mid][mid_element]:
                        right = mid_element - 1
                    else:
                        return True
                return False
        return False