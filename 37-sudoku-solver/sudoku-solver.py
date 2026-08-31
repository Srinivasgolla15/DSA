class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        # rows = [set() for _ in range(9)]
        # cols = [set() for _ in range(9)]
        # boxes = [set() for _ in range(9)]

        # # Build the initial state
        # for r in range(9):
        #     for c in range(9):
        #         if board[r][c] != ".":
        #             num = board[r][c]

        #             rows[r].add(num)
        #             cols[c].add(num)

        #             box = (r // 3) * 3 + (c // 3)
        #             boxes[box].add(num)

        # def dfs(r, c):

        #     # If we reached row 9, entire board is solved
        #     if r == 9:
        #         return True

        #     # Move to next row after column 8
        #     if c == 9:
        #         return dfs(r + 1, 0)

        #     # Already filled cell
        #     if board[r][c] != ".":
        #         return dfs(r, c + 1)

        #     box = (r // 3) * 3 + (c // 3)

        #     # Try every number
        #     for num in "123456789":

        #         # Number already exists
        #         if num in rows[r] or num in cols[c] or num in boxes[box]:
        #             continue

        #         # Place number
        #         board[r][c] = num
        #         rows[r].add(num)
        #         cols[c].add(num)
        #         boxes[box].add(num)

        #         # Move to next cell
        #         if dfs(r, c + 1):
        #             return True

        #         # Backtrack
        #         board[r][c] = "."
        #         rows[r].remove(num)
        #         cols[c].remove(num)
        #         boxes[box].remove(num)

        #     return False

        # dfs(0, 0)


# Time: O(9^E), where E = number of empty cells
# Space: O(81) = O(1), for row/column/box sets + recursion stack

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty.append((i, j))
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[(i // 3) * 3 + j // 3].add(board[i][j])

        def backtrack(index):
            if index == len(empty):
                return True

            r, c = empty[index]
            box = (r // 3) * 3 + c // 3

            for num in "123456789":
                if num not in rows[r] and num not in cols[c] and num not in boxes[box]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)

                    if backtrack(index + 1):
                        return True

                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box].remove(num)

            return False

        backtrack(0)