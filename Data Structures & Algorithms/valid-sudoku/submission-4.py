class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for element in range(9):
                if board[row][element] == ".":
                    continue
                if board[row][element] in seen:
                    return False
                seen.add(board[row][element])
        
        for col in range(9):
            seen = set()
            for element in range(9):
                if board[element][col] == ".":
                    continue
                if board[element][col] in seen:
                    return False
                seen.add(board[element][col])

        starts = [(0,0), (0,3), (0,6),
                (3,0), (3,3), (3,6),
                (6,0), (6,3), (6,6)]

        for i,j in starts:
            seen = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        return True

        