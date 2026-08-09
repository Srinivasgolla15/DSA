class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        cols = set()
        dia1 = set()
        dia2 = set()
        count = [0]
        def dfs(row):
            if row == n:
                count[0]+=1
                return 
            
            for col in range(n):
                if (col not in cols and (row - col) not in dia1 and
                    (row + col) not in dia2):
                    cols.add(col)
                    dia1.add(row-col)
                    dia2.add(row+col)

                    dfs(row+1)

                    cols.remove(col)
                    dia1.remove(row - col)
                    dia2.remove(row + col)
        dfs(0)
        return count[0]
