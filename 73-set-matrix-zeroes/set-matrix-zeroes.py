class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

# --------------- HASHSET O(mn) time, O(m+n) space --------------
        rows = set()
        cols = set()

        m = len(matrix)
        n = len(matrix[0])

       
        # Store every row and column containing a zero.
        for i in range(m):
            for j in range(n):

                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
 
        # If current row or column contains a zero,
        # make the current cell zero.
        for i in range(m):
            for j in range(n):

                if i in rows or j in cols:
                    matrix[i][j] = 0

        