class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # rows,cols = len(grid),len(grid[0])
     
        # count = 0
        # directions = [(1,0),(0,1),(-1,0),(0,-1)]
        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j]==2:
        #             count+=1
        #             for d in directions:
        #                 nr,nc = i+d[0],j+d[1]
        #                 if nr>=rows or nc>=cols or nr<0 or nc<0:
        #                     continue
        #                 grid[nr][nc] == 2
                 
                    
        # not ideal for DFS only in BFS even for interview level
        # row,col=len(grid),len(grid[0])
        # count=0
        # def dfs(r,c):
        #     if r < 0 or c < 0 or r >= row or c >= col:
        #         return
        #     if grid[r][c] != 1:
        #         return
        #     grid[r][c]=2
        #     dfs(r-1,c)
        #     dfs(r+1,c)
        #     dfs(r,c-1)
        #     dfs(r,c+1)
        # for r in range(row):
        #     for c in range(col):

        #         if grid[r][c] == 2:
        #             count+=1

        #             dfs(r+1, c)
        #             dfs(r-1, c)
        #             dfs(r, c+1)
        #             dfs(r, c-1)
        # for i in range(row):
        #     for j in range(col):
        #         if grid[i][j]==1:
        #             count=-1
        # return count
    # ------------------------------------------------------------------------------>
        # rows, cols = len(grid), len(grid[0])

        # # queue for BFS
        # dq = deque()

        # # count fresh oranges
        # fresh = 0

        # # find all fresh and rotten oranges
        # for i in range(rows):
        #     for j in range(cols):

        #         # fresh orange
        #         if grid[i][j] == 1:
        #             fresh += 1

        #         # rotten orange
        #         elif grid[i][j] == 2:
        #             dq.append((i, j))

        # # no fresh oranges already
        # if fresh == 0:
        #     return 0

        # # total minutes
        # time = 0

        # # BFS
        # while dq and fresh > 0:

        #     # current level size
        #     # all these oranges rot others in SAME minute
        #     size = len(dq)

        #     # process one BFS level
        #     for _ in range(size):

        #         r, c = dq.popleft()

        #         # 4 directions
        #         directions = [(1,0),(-1,0),(0,1),(0,-1)]

        #         for dr, dc in directions:

        #             nr, nc = r + dr, c + dc

        #             # valid fresh orange
        #             if (0 <= nr < rows and
        #                 0 <= nc < cols and
        #                 grid[nr][nc] == 1):

        #                 # make orange rotten
        #                 grid[nr][nc] = 2

        #                 # one fresh orange removed
        #                 fresh -= 1

        #                 # add newly rotten orange
        #                 # for next minute processing
        #                 dq.append((nr, nc))

        #     # one full minute completed
        #     time += 1

        # # some fresh oranges could not rot
        # if fresh > 0:
        #     return -1

        # return time
# Time Complexity: O(m * n)
# - Every cell is visited at most once.

# Space Complexity: O(m * n)
# - BFS queue can contain up to all cells in the grid.


# -----------------------------------------
  
        rows, cols = len(grid), len(grid[0])

        dq = deque()

        # Add all initially rotten oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    dq.append((i, j))

        if not dq:
            # No rotten oranges initially
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1:
                        return -1
            return 0

        time = 0

        while dq:
            size = len(dq)
             

            for _ in range(size):
                r, c = dq.popleft()

                directions = [(1,0), (-1,0), (0,1), (0,-1)]

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == 1):

                        grid[nr][nc] = 2
                        dq.append((nr, nc))
                        
 
            time += 1

        # Check whether any fresh orange remains
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1

        return time-1



                