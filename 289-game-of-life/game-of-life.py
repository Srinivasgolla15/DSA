class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])
        directions = [(0,1),(1,0),(1,1),(0,-1),(-1,0),(1,-1),(-1,1),(-1,-1)]
        newboard = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                count = 0
                for d in directions:
                    r = i + d[0]
                    c = j + d[1]
                    if r >= m or r < 0 or c < 0 or c >= n:
                        continue
                    if board[r][c] == 1:
                        count += 1

                if board[i][j] == 0:
                    if count == 3:
                        newboard[i][j] = 1

                else:
                    if count == 2 or count == 3:
                        newboard[i][j] = 1

        for i in range(m):
            for j in range(n):
                board[i][j] = newboard[i][j]