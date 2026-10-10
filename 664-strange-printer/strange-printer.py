class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return 0

        # Remove consecutive duplicate characters
        arr = []
        for ch in s:
            if not arr or arr[-1] != ch:
                arr.append(ch)

        s = "".join(arr)
        n = len(s)
        memo = {}

        def dfs(i, j):
            if i > j:
                return 0

            if i == j:
                return 1

            if (i, j) in memo:
                return memo[(i, j)]

            # Option 1: print s[i] separately
            ans = 1 + dfs(i + 1, j)

            # Option 2: combine s[i] with a matching character
            for k in range(i + 1, j + 1):
                if s[i] == s[k]:

                    middle = dfs(i + 1, k - 1)
                    right = dfs(k, j)

                    ans = min(ans, middle + right)

            memo[(i, j)] = ans
            return ans

        return dfs(0, n - 1)


# Time Complexity: O(N^3)
# Space Complexity: O(N^2) for memoization
# Recursion stack: O(N)