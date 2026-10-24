class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        queens = [-1] * n 
        cols = [False] * n
        pos_diag = [False] * (2 * n) 
        neg_diag = [False] * (2 * n) 
        def backtrack(r: int):
            if r == n:
                res.append(["." * c + "Q" + "." * (n - c - 1) for c in queens])
                return
            for c in range(n):
                if cols[c] or pos_diag[r + c] or neg_diag[r - c + n]:
                    continue              
                cols[c] = pos_diag[r + c] = neg_diag[r - c + n] = True
                queens[r] = c
                backtrack(r + 1)            
                cols[c] = pos_diag[r + c] = neg_diag[r - c + n] = False
        backtrack(0)
        return res
