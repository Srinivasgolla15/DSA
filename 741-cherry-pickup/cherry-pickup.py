class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

# WRONG IMPLEMENTATION ------


        # m = len(grid)
        # n= len(grid[0])
        # count = [0]
        
       
        # def checkpath(i,j):
        #     if i==m-1 and j==n-1:
        #         return dfs(i,j)
          
        #     if i>=m or j >=n or grid[i][j]==-1:
        #         return
            
        #     if grid[i][j]==0 or grid[i][j] == 1:
        #         checkpath(i+1,j) or checkpath(i,j+1)
        #     return False

        # def dfs(i,j):
           
        #     if i<0 or j<0 or grid[i][j]==-1:
        #         return
        #     if grid[i][j]==0:
                
        #         dfs(i-1,j) or dfs(i,j-1)
        #     if grid[i][j]==1:
                
        #         count[0]+=1
        #         dfs(i-1,j) or dfs(i,j-1)
        # checkpath(0,0)
        # return count[0]


# ----------Brute Force using .copy()-----------
# Time Limit Exceeded 18 / 60
# O(2^(N^2)) approximately, for each forward/return path combination

# 3D DP:
# O(N^3) time
# O(N^3) space

        # m = len(grid)
        # n = len(grid[0])

        # def return_trip(i, j, collected):

        #     # Reached starting cell
        #     if i == 0 and j == 0:
        #         return 0

        #     # Invalid cell
        #     if i < 0 or j < 0 or grid[i][j] == -1:
        #         return float("-inf")

        #     cherry = 0

        #     # Pick this cherry only if it wasn't picked
        #     # during the forward trip
        #     if grid[i][j] == 1 and (i, j) not in collected:
        #         cherry = 1

        #     return cherry + max(
        #         return_trip(i - 1, j, collected),
        #         return_trip(i, j - 1, collected)
        #     )

        # def forward_trip(i, j, collected, cherries):

        #     # Invalid
        #     if i >= m or j >= n or grid[i][j] == -1:
        #         return float("-inf")

        #     # Collect current cherry
        #     new_collected = collected.copy()
        #     new_cherries = cherries

        #     if grid[i][j] == 1:
        #         new_collected.add((i, j))
        #         new_cherries += 1

        #     # Reached destination
        #     if i == m - 1 and j == n - 1:

        #         # Forward cherries + new cherries on return
        #         return new_cherries + return_trip(
        #             i, j, new_collected
        #         )

        #     # Continue forward
        #     return max(
        #         forward_trip(
        #             i + 1,
        #             j,
        #             new_collected,
        #             new_cherries
        #         ),
        #         forward_trip(
        #             i,
        #             j + 1,
        #             new_collected,
        #             new_cherries
        #         )
        #     )

        # return max(0, forward_trip(0, 0, set(), 0))

# ----------Brute Force using Backtracking-----------
# Time Limit Exceeded 18 / 60 
        # m = len(grid)
        # n = len(grid[0])

        # def return_trip(i, j, collected):

        #     # Reached starting point
        #     if i == 0 and j == 0:
        #         return 0

        #     # Invalid
        #     if i < 0 or j < 0 or grid[i][j] == -1:
        #         return float("-inf")

        #     cherry = 0

        #     # Collect only if not collected during first trip
        #     if grid[i][j] == 1 and (i, j) not in collected:
        #         cherry = 1

        #     return cherry + max(
        #         return_trip(i - 1, j, collected),
        #         return_trip(i, j - 1, collected)
        #     )

        # def forward_trip(i, j, collected, cherries):

        #     # Invalid
        #     if i >= m or j >= n or grid[i][j] == -1:
        #         return float("-inf")

        #     # Copy the current state
        #     new_collected = collected.copy()
        #     new_cherries = cherries

        #     # Collect current cherry
        #     if grid[i][j] == 1:
        #         new_collected.add((i, j))
        #         new_cherries += 1

        #     # Reached destination
        #     if i == m - 1 and j == n - 1:

        #         return new_cherries + return_trip(
        #             i,
        #             j,
        #             new_collected
        #         )

        #     # Explore both paths
        #     return max(
        #         forward_trip(
        #             i + 1,
        #             j,
        #             new_collected,
        #             new_cherries
        #         ),
        #         forward_trip(
        #             i,
        #             j + 1,
        #             new_collected,
        #             new_cherries
        #         )
        #     )

        # ans = forward_trip(0, 0, set(), 0)

        # return max(0, ans)

        

        m = len(grid)
        n = len(grid[0])
        memo = {}

        def dfs(r1, c1, r2, c2):

            # invalid
            if (
                r1 >= m or c1 >= n or
                r2 >= m or c2 >= n or
                grid[r1][c1] == -1 or
                grid[r2][c2] == -1
            ):
                return float("-inf")

            state = (r1, c1, r2, c2)

            if state in memo:
                return memo[state]

            # collect cherries
            cherries = grid[r1][c1]

            if (r1, c1) != (r2, c2):
                cherries += grid[r2][c2]

            # reached destination
            if r1 == m - 1 and c1 == n - 1:
                return cherries

            # four possibilities
            best = max(
                dfs(r1 + 1, c1,     r2 + 1, c2),
                dfs(r1 + 1, c1,     r2,     c2 + 1),
                dfs(r1,     c1 + 1, r2 + 1, c2),
                dfs(r1,     c1 + 1, r2,     c2 + 1)
            )

            memo[state] = cherries + best
            return memo[state]

        return max(0, dfs(0, 0, 0, 0))
        

            