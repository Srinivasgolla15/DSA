class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """

        memo = {}

        def dfs(i, m, n):

            # No more strings
            if i == len(strs):
                return 0

            # Already solved this state
            if (i, m, n) in memo:
                return memo[(i, m, n)]

            zeros = strs[i].count('0')
            ones = strs[i].count('1')

            # Skip current string
            skip = dfs(i + 1, m, n)

            # Take current string if it fits
            take = 0
            if zeros <= m and ones <= n:
                take = 1 + dfs(
                    i + 1,
                    m - zeros,
                    n - ones
                )

            memo[(i, m, n)] = max(skip, take)

            return memo[(i, m, n)]

        return dfs(0, m, n)