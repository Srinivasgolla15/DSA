class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

# -------------------- DFS+ MEMOIZATION -------------------- 

# Time Complexity: O(m * n)
# - There are m * n cells.
# - Each cell's DFS is calculated only once because of memoization.
# - For each cell, we check 4 directions.
# - 4 is constant, so total = O(m * n).
#
# Space Complexity: O(m * n)
# - memo stores the answer for every cell: O(m * n)
# - Recursion stack can be O(m * n) in the worst case.
#
# Overall:
# Time  = O(m * n)
# Space = O(m * n)
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        memo = {}
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def dfs(i,j):
            
            count = 1
            curr = matrix[i][j]
            if (i,j) in memo:
                return memo[(i,j)]
            
            for r,c in directions:
                nr,nc = i+r,j+c
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                 
                if matrix[nr][nc] > curr:
                    count = max(count,1+dfs(nr,nc))
            memo[(i,j)] = count
            return count
        answer = 0

        for i in range(m):
            for j in range(n):
                answer = max(answer, dfs(i, j))

        return answer
        

                