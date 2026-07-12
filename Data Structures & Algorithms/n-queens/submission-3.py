class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        posDiaSet = set()
        negDiaSet = set()
        colSet = set()

        grid = [["."] * n for i in range(n)]
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
                posDiaSet.add(r + c)
                negDiaSet.add(r - c)
                colSet.add(c)
                
                dfs(r + 1)

                colSet.remove(c)
                negDiaSet.remove(r - c)
                posDiaSet.remove(r + c)
                grid[r][c] = "."

        dfs(0)
        return res
        