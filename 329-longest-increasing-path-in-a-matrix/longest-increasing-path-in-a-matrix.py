class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

# ---------------
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
        

                