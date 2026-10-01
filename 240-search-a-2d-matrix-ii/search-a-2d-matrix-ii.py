class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

# -------------------Binary Search row by row-----------------------
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):

            low = 0
            high = cols - 1

            while low <= high:
                mid = (low + high) // 2

                if matrix[row][mid] == target:
                    return True

                elif matrix[row][mid] > target:
                    high = mid - 1

                else:
                    low = mid + 1

        return False


        