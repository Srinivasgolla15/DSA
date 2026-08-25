class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
# ---------------brute-force DFS + partitioning (TLE)-------------
#  Time:
#   O(N * 2^N)
#
#   At every position we have roughly 2 choices:
#       1. cut
#       2. don't cut
#
#   This creates O(2^N) possible partition choices.
#
#   Additionally, ispalindrome() can take O(N).
#
#   Therefore a safe bound is O(N * 2^N).
#
# Space:
#   O(N)
#
#   Recursion depth can reach N.
#   The temporary substring checks do not create
#   a stored DP table.
# ------------------------

        # def ispalindrome(string):
        #     left = 0
        #     right = len(string)-1
        #     while left<right:
        #         if string[left] == string[right]:
        #             left+=1
        #             right-=1
        #         else:
        #             return False
        #     return True
         
        # def dfs(k,prev):
        #     if k == len(s)-1:
        #         if ispalindrome(s[prev:k+1]):
        #             return 0
                # Invalid partition
        #         return float('inf')
        #     skip = dfs(k+1,prev)
        #     if ispalindrome(s[prev:k+1]): 
        #         take = 1+dfs(k+1,k+1)
                
        #         return min(take,skip)
        #     return skip
        # return dfs(0,0)


# --------------memoization  (TLE) ----------------
        # def ispalindrome(string):
        #     left = 0
        #     right = len(string)-1
        #     while left<right:
        #         if string[left] == string[right]:
        #             left+=1
        #             right-=1
        #         else:
        #             return False
        #     return True
        # memo = {}
        # def dfs(k,prev):
        #     if (k, prev) in memo:
        #         return memo[(k, prev)]

        #     if k == len(s)-1:
        #         if ispalindrome(s[prev:k+1]):
        #             return 0
        #          # Invalid partition
        #         return float('inf')
        #     skip = dfs(k+1,prev)
        #     if ispalindrome(s[prev:k+1]):
        #          # Make one cut 
        #         take = 1+dfs(k+1,k+1)
                
        #         return min(take,skip)
        #     else:
        #          # Cannot cut because current substring
        #         # is not a palindrome
        #         return skip
            
        #     memo[(k, prev)] = ans
        #     return ans
        # return dfs(0,0)



        # n = len(s)
        # pal = [[False] * n for _ in range(n)]

        # # Fill from bottom to top because
        # # pal[i][j] depends on pal[i+1][j-1]
        # for i in range(n - 1, -1, -1):

        #     for j in range(i, n):

        #         # First and last characters must match
        #         # and the inside must also be palindrome
        #         if s[i] == s[j] and (
        #             j - i <= 2 or pal[i + 1][j - 1]
        #         ):
        #             pal[i][j] = True

        # # memo[(k, prev)] = minimum cuts from this state
        # memo = {}

        # # dfs(k, prev):
        # # s[prev:k+1] is the current substring
        # def dfs(k, prev):

        #     # Already solved this state
        #     if (k, prev) in memo:
        #         return memo[(k, prev)]

        #     # Reached the last character
        #     if k == n - 1:

        #         # Remaining substring is palindrome
        #         # so no more cuts are needed
        #         if pal[prev][k]:
        #             return 0

        #         # Invalid partition
        #         return float('inf')

        #     # Don't cut here
        #     # Extend the current substring
        #     skip = dfs(k + 1, prev)

        #     # Cut here only if current substring is palindrome
        #     if pal[prev][k]:

        #         # +1 = make one cut
        #         # Next substring starts at k+1
        #         take = 1 + dfs(k + 1, k + 1)

        #         ans = min(take, skip)

        #     else:
        #         # Cannot cut because current substring
        #         # is not a palindrome
        #         ans = skip

        #     # Store result for this state
        #     memo[(k, prev)] = ans

        #     return ans

        # return dfs(0, 0)


# ---------------------------------------------------------
# Approach:
# Palindrome 2DP + Memoized DFS
#
# Time Complexity:
# O(N²)
#
# 1. Build palindrome table → O(N²)
# 2. Number of DFS states → O(N²)
# 3. Palindrome lookup pal[i][j] → O(1)
#
# Therefore:
# O(N²)
#
# Space Complexity:
# O(N²)



        n = len(s)

        # ---------------- Palindrome DP ----------------
        # pal[i][j] = True if s[i:j+1] is a palindrome
        # Time: O(n^2), Space: O(n^2)
        pal = [[False] * n for _ in range(n)]

        # Build palindrome table from smaller substrings to larger ones
        for i in range(n - 1, -1, -1):
            for j in range(i, n):

                # Ends must match, and middle must also be palindrome
                if s[i] == s[j] and (j - i <= 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True


        # ---------------- 1D DP ----------------
        # dp[i] = minimum cuts needed for s[0:i+1]
        #
        # For every i, try every palindrome s[j:i+1]
        # as the LAST part of the partition.
        #
        # If s[j:i+1] is palindrome:
        #     cuts = dp[j-1] + 1
        #
        # dp[j-1] -> cuts needed for the part before palindrome
        # +1      -> cut between the two parts
        #
        # Time: O(n^2), Space: O(n)
        dp = [0] * n

        for i in range(n):

            # Entire s[0:i+1] is already a palindrome
            # so no cut is needed.
            if pal[0][i]:
                dp[i] = 0
                continue

            # Worst case: cut between every character
            dp[i] = i

            # Try every possible starting point j
            # for the LAST palindrome ending at i.
            for j in range(1, i + 1):

                if pal[j][i]:

                    # s[j:i+1] is the last palindrome
                    # dp[j-1] solves everything before it
                    dp[i] = min(dp[i], dp[j - 1] + 1)

        # Total minimum cuts for the entire string
        #
        # Overall Time:  O(n^2)
        # Overall Space: O(n^2)
        return dp[n - 1]


