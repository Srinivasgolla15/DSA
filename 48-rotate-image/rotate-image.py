class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None
        """

        n = len(matrix)

        # Process one layer at a time
        for layer in range(n // 2):

            first = layer
            last = n - 1 - layer

            # Rotate every element in this layer
            for i in range(first, last):

                offset = i - first

                # Save the top element
                top = matrix[first][i]

                # Left -> Top
                matrix[first][i] = matrix[last - offset][first]

                # Bottom -> Left
                matrix[last - offset][first] = matrix[last][last - offset]

                # Right -> Bottom
                matrix[last][last - offset] = matrix[i][last]

                # Top -> Right
                matrix[i][last] = top