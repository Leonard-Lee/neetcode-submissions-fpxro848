class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colSet = set()
        posDiagSet = set() # r + c
        negDiagSet = set() # r - c

        res = []
        grid = [["."] * n for i in range(n)]

        def dfs(r) -> None:
            if r == n:
                tmp = []
                for i in range(n):
                    tmp.append("".join(grid[i]))
                res.append(tmp)
                return

            for c in range(n):
                if c in colSet or r + c in posDiagSet or r - c in negDiagSet:
                    continue

                colSet.add(c)
                posDiagSet.add(r + c)
                negDiagSet.add(r - c)

                grid[r][c] = "Q"
                dfs(r + 1)
                grid[r][c] = "."

                colSet.remove(c)
                posDiagSet.remove(r + c)
                negDiagSet.remove(r - c)

        dfs(0)
        return res
            
        