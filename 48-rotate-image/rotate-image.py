class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        j =0
        res = []
        n =len(matrix[0])
        while j<n:
            arr = []
            for i in range(n-1,-1,-1):
                arr.append(matrix[i][j])
            j+=1
            res.append(arr)
        matrix[:]=res