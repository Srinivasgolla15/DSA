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
        # n = len(s)
        # m = len(t)

        # if m > n:
        #     return 0

        # memo = {}

        # def dfs(i, j):

        #     if (i, j) in memo:
        #         return memo[(i, j)]

        #     if j == m:
        #         return 1

        #     if i == n or (m - j > n - i):
        #         return 0

        #     if s[i] == t[j]:
        #         take = dfs(i + 1, j + 1)
        #         skip = dfs(i + 1, j)
        #         memo[(i, j)] = take + skip
        #     else:
        #         memo[(i, j)] = dfs(i + 1, j)

        #     return memo[(i, j)]

        # return dfs(0, 0)

# ---------------TABULATION -------------------
        # n = len(s)
        # m = len(t)

        # # If target is longer than source,
        # # it's impossible to form t
        # if m > n:
        #     return 0

        # # -------------------------------------------------------
        # # dp[i][j] = Number of ways to form t[j:]
        # #            using s[i:]
        # #
        # # Extra row  -> i == n (source exhausted)
        # # Extra col  -> j == m (target exhausted)
        # # -------------------------------------------------------
        # dp = [[0] * (m + 1) for _ in range(n + 1)]

        # # ---------------- Base Case ----------------
        # # Empty target ("") can always be formed
        # # by choosing nothing from any suffix of s.
        # #
        # # Therefore:
        # # dp[i][m] = 1 for every i
        # for i in range(n + 1):
        #     dp[i][m] = 1

        # # ---------------- Fill DP Table ----------------
        # # Fill from Bottom -> Top because
        # # current row depends on the row below.
        # for i in range(n - 1, -1, -1):

        #     # Fill from Right -> Left because
        #     # current cell depends on j+1.
        #     for j in range(m - 1, -1, -1):

        #         # Characters match
        #         if s[i] == t[j]:

        #             # Take current character
        #             # +
        #             # Skip current character
        #             dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]

        #         else:
        #             # Characters don't match,
        #             # so we must skip s[i]
        #             dp[i][j] = dp[i + 1][j]

        # # dp[0][0] = Number of ways to form
        # # the entire target using the entire source
        # return dp[0][0]


# ----------SPACE OPTIMIZED----------------
        n = len(s)
        m = len(t)

        # Impossible if target is longer than source
        if m > n:
            return 0

        # --------------------------------------------------
        # dp[j] = Number of ways to form t[j:]
        #         using the current suffix of s
        #
        # Initially, dp represents the last row (i = n).
        # --------------------------------------------------
        dp = [0] * (m + 1)

        # Base Case:
        # Empty target can always be formed in one way.
        dp[m] = 1

        # Process rows from bottom to top
        for i in range(n - 1, -1, -1):

            # prev stores dp[i+1][j+1] (diagonal value)
            prev = dp[m]

            # Traverse columns from right to left
            for j in range(m - 1, -1, -1):

                # Save old dp[j] before overwriting.
                # This is dp[i+1][j].
                temp = dp[j]

                if s[i] == t[j]:
                    # Take current character
                    # +
                    # Skip current character
                    dp[j] = prev + dp[j]

                # Else:
                # dp[j] already represents dp[i+1][j],
                # so nothing needs to be changed.

                # Move diagonal for next iteration
                prev = temp

        # Number of ways to form entire t from entire s
        return dp[0]
