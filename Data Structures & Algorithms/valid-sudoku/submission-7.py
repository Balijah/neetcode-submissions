class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
        
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in seen:
                    return False
                seen.add(board[j][i])
        
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