class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colSet = set()
        posDiagSet = set() # r + c
        negDiagSet = set() # r - c

        res = []
        grid = [["."] * n for i in range(n)]
        def backtrack(r : int) -> None:
            if r == n:
                copy = ["".join(row) for row in grid]
                res.append(copy)
                return
            
            for c in range(n):
                if c in colSet or r + c in posDiagSet or r - c in negDiagSet:
                    continue

                colSet.add(c) 
                posDiagSet.add(r + c)
                negDiagSet.add(r - c)
                grid[r][c] = "Q"

                backtrack(r + 1)

                grid[r][c] = "."
                negDiagSet.remove(r - c)
                posDiagSet.remove(r + c)
                colSet.remove(c) 

        backtrack(0)
        return res

                



        