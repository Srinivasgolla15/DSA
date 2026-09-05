class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            self.prefix = []
            return

        rows = len(matrix)
        cols = len(matrix[0])

        # Extra row and column make boundary cases easy
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(rows):
            for j in range(cols):

                # Current value
                # + everything above
                # + everything to the left
                # - top-left overlap
                self.prefix[i + 1][j + 1] = (
                    matrix[i][j]
                    + self.prefix[i][j + 1]
                    + self.prefix[i + 1][j]
                    - self.prefix[i][j]
                )

        # Time: O(rows * cols)
        # Space: O(rows * cols)

        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # Big rectangle
        total = self.prefix[row2 + 1][col2 + 1]

        # Remove area above
        total -= self.prefix[row1][col2 + 1]

        # Remove area to the left
        total -= self.prefix[row2 + 1][col1]

        # Add back top-left overlap
        total += self.prefix[row1][col1]

        return total

        # Time: O(1)
        # Space: O(1)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)