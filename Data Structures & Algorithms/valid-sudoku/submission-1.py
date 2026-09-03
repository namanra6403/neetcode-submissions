class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue

                box_key = (r // 3, c // 3)

                if board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in boxes[box_key]:
                    return False
                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                boxes[box_key].add(board[r][c])

        return True
