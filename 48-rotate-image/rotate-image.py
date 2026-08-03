class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

# --------Auxiliary Matrix (Extra Matrix) Approach -----------
# Time Complexity: O(n²)
# Space Complexity: O(n²)
        # j =0
        # res = []
        # n =len(matrix[0])
        # while j<n:
        #     arr = []
        #     for i in range(n-1,-1,-1):
        #         arr.append(matrix[i][j])
        #     j+=1
        #     res.append(arr)
        # matrix[:]=res

# -------------Transpose + Reverse Each Row (In-place)------------
# Time: O(n²)
# Space: O(1)
        n = len(matrix)

        # ---------------- Transpose ----------------
        # Swap matrix[i][j] with matrix[j][i]
        # Only visit the upper triangle to avoid swapping twice.
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # ---------------- Reverse each row ----------------
        for i in range(n):
            matrix[i].reverse()
