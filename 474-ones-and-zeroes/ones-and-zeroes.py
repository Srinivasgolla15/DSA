class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """

        # memo = {}

        # def dfs(i, m, n):

        #     # No more strings
        #     if i == len(strs):
        #         return 0

        #     # Already solved this state
        #     if (i, m, n) in memo:
        #         return memo[(i, m, n)]

        #     zeros = strs[i].count('0')
        #     ones = strs[i].count('1')

        #     # Skip current string
        #     skip = dfs(i + 1, m, n)

        #     # Take current string if it fits
        #     take = 0
        #     if zeros <= m and ones <= n:
        #         take = 1 + dfs(
        #             i + 1,
        #             m - zeros,
        #             n - ones
        #         )

        #     memo[(i, m, n)] = max(skip, take)

        #     return memo[(i, m, n)]

        # return dfs(0, m, n)

# Time Complexity: O(k * m * n * L)
# k = number of strings
# m = maximum number of 0s
# n = maximum number of 1s
# L = average length of a string
#
# Space Complexity: O(k * m * n)
# memo stores at most k * m * n states
# Recursion stack: O(k)


# ---------------BOTTOM UP --------------------
        # dp[z][o] = maximum number of strings
        # we can select using at most z zeros and o ones
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Process each string one by one
        for string in strs:

            # Cost of choosing this string
            zeros = string.count('0')
            ones = string.count('1')

            # Go backwards so the same string is not used twice
            for z in range(m, zeros - 1, -1):
                for o in range(n, ones - 1, -1):

                    # Skip the string:
                    # dp[z][o]
                    #
                    # Take the string:
                    # 1 + dp[z - zeros][o - ones]
                    #
                    # Choose whichever gives more strings
                    dp[z][o] = max(
                        dp[z][o],
                        1 + dp[z - zeros][o - ones]
                    )

        return dp[m][n]

        # Time Complexity: O(k * m * n * L)
        # k = number of strings
        # L = average length of each string
        #
        # Space Complexity: O(m * n)
        # 2D DP table
        