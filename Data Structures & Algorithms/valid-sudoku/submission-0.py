class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        isDuplicateSet = set()
        for i in range(9):
            isDuplicateSet = set()
            for j in range(9):
                if board[i][j] == ".": continue
                if board[i][j] in isDuplicateSet:
                    return False
                else:
                    isDuplicateSet.add(board[i][j])

        # column
        isDuplicateSet = set()
        for j in range(9):
            isDuplicateSet = set()
            for i in range(9):
                if board[i][j] == ".": continue
                if board[i][j] in isDuplicateSet:
                    return False
                else:
                    isDuplicateSet.add(board[i][j])
        
        # sub-boxes
        isDuplicateDict = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": continue
                key = str(i // 3) + str(j // 3)
                val = isDuplicateDict[key]
                if board[i][j] in val:
                    return False
                else:
                    isDuplicateDict[key].add(board[i][j])
        return True