class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

# ---------------BRUTEFORCE (TLE & string insertion everytime)---
# Time = O(2^n)
# spcae = O(n)
        # count = [0]
        # if len(t)>len(s):
        #     return 0
        # def dfs(i,string):
             
        #     if string == t:
        #         count[0]+=1
        #         return 
        #     if i == len(s):
        #         return
            
        
        #     take = dfs(i+1,string+s[i])
        #     skip = dfs(i+1,string)
        #     take or skip
        # dfs(0,"")
        # return count[0]

# ------------RECURSION TLE----------
        # count = [0]
        # n = len(s)
        # m = len(t)
        # if m>n:
        #     return 0
        # def dfs(i,j):
        #     if i==n and j< m :
        #         return
        #     if j==m:
        #         count[0]+=1
        #         return 
        #     if  s[i] == t[j]:
        #         dfs(i+1,j+1)
        #     dfs(i+1,j)
             
        # dfs(0,0)
        # return count[0]     


# --------------MEMOIZATION --------------------
# Time: O(n × m)
# Space: O(n × m) (memo) + O(n) recursion stack
        n = len(s)
        m = len(t)

        if m > n:
            return 0

        memo = {}

        def dfs(i, j):

            if (i, j) in memo:
                return memo[(i, j)]

            if j == m:
                return 1

            if i == n or (m - j > n - i):
                return 0

            if s[i] == t[j]:
                take = dfs(i + 1, j + 1)
                skip = dfs(i + 1, j)
                memo[(i, j)] = take + skip
            else:
                memo[(i, j)] = dfs(i + 1, j)

            return memo[(i, j)]

        return dfs(0, 0)

# ---------------TABULATION -------------------


        