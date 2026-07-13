class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [["."] * n for i in range(n)]

        colSet = set()
        posDiaSet = set() # (r + c)
        negDiaSet = set() # (r - c)

        res = []
        def dfs(r: int) -> None:
            if r == n:
                tmp = []
                for i in range(n):
                    tmp.append("".join(grid[i]))
                res.append(tmp)
                return

            for c in range(n):
                if c in colSet or (r + c) in posDiaSet or (r - c) in negDiaSet:
                    continue 

                grid[r][c] = "Q"
                colSet.add(c)
                posDiaSet.add((r + c))
                negDiaSet.add((r - c))

                dfs(r + 1)

                negDiaSet.remove((r - c))
                posDiaSet.remove((r + c))
                colSet.remove(c)
                grid[r][c] = "."

        dfs(0)
        return res
        
        