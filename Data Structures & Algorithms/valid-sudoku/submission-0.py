class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols= defaultdict(set)
        threebythree = defaultdict(set)

        for row in range(9):
            for column in range(9):
                val = board[row][column]

                if val == ".":
                    continue

                if (val in rows[row] or val in cols[column] or val in threebythree[row//3, column//3]):
                    return False

                rows[row].add(val)
                cols[column].add(val)
                threebythree[row//3, column//3].add(val)

        return True
        