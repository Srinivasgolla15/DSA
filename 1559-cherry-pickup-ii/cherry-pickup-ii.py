class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        rows, cols = len(grid), len(grid[0])

        memo = {}

        def dfs(r, c1, c2):

            if r == rows:
                return 0

            # Check whether state already exists
            if (r, c1, c2) in memo:
                return memo[(r, c1, c2)]

            cherries = grid[r][c1]

            if c1 != c2:
                cherries += grid[r][c2]

            maxi = 0

            for d1 in [-1, 0, 1]:
                for d2 in [-1, 0, 1]:

                    nc1 = c1 + d1
                    nc2 = c2 + d2

                    if 0 <= nc1 < cols and 0 <= nc2 < cols:

                        maxi = max(maxi, dfs(r + 1, nc1, nc2))

            memo[(r, c1, c2)] = cherries + maxi

            return memo[(r, c1, c2)]

        return dfs(0, 0, cols - 1)


# Time Complexity: O(rows * cols^2 * 9)
#                 = O(rows * cols^2)
#
# Space Complexity: O(rows * cols^2) for memo
#                    O(rows) recursion stack

        