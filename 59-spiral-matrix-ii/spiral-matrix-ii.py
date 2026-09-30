class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

#--------------------------Direction + visited set O(n2) O(n2)----------------------------

        # matrix = [[0] * n for _ in range(n)]
        # visited = set()

        # directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # r = 0
        # c = 0
        # direction = 0

        # for value in range(1, n * n + 1):

        #     matrix[r][c] = value
        #     visited.add((r, c))

        #     nr = r + directions[direction][0]
        #     nc = c + directions[direction][1]

        #     if (nr < 0 or nr >= n or
        #         nc < 0 or nc >= n or
        #         (nr, nc) in visited):

        #         direction = (direction + 1) % 4

        #         nr = r + directions[direction][0]
        #         nc = c + directions[direction][1]

        #     r = nr
        #     c = nc

        # return matrix




# --------------------Four Boundaries O(n2) O(1) ---------------------------------

        matrix = [[0] * n for _ in range(n)]

        top = 0
        bottom = n - 1
        left = 0
        right = n - 1

        num = 1

        while top <= bottom and left <= right:

            # → Right
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1

            top += 1

            # ↓ Down
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1

            right -= 1

            # ← Left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = num
                    num += 1

                bottom -= 1

            # ↑ Up
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = num
                    num += 1

                left += 1

        return matrix

        