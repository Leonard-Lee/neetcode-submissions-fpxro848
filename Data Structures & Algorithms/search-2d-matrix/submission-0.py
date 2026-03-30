class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        m = len(matrix)
        n = len(matrix[0])

        l, r = 0, m * n - 1
        while l <= r:
            m = l + ((r - l) // 2)
            row = m // n
            col = m % n
            if matrix[row][col] < target:
                l = m + 1
            elif matrix[row][col] > target:
                r = m - 1
            else:
                return True
        return False
        