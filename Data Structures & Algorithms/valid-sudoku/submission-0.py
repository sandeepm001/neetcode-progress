class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)

        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x=='.':
                    continue
                k = (i//3,j//3)
                if x in rows[i] or x in cols[j] or x in box[k]:
                    return False
                rows[i].add(x)
                cols[j].add(x)
                box[k].add(x)
        return True
