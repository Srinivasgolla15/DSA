 
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        m = len(s)
        n = len(p)

        memo = {}

        def dfs(i, j):

            # Both string and pattern are completely consumed
            if i == m and j == n:
                return True

            # Pattern is finished but string is still remaining
            if j == n:
                return False

            if (i, j) in memo:
                return memo[(i, j)]

            # Does current character match?
            if i < m and (s[i] == p[j] or p[j] == "."):

                # Is current character followed by '*'?
                if j + 1 < n and p[j + 1] == "*":

                    # Option 1: use zero occurrences
                    skip = dfs(i, j + 2)

                    # Option 2: use one occurrence
                    take = dfs(i + 1, j)

                    memo[(i, j)] = skip or take

                else:
                    # Normal character / '.'
                    memo[(i, j)] = dfs(i + 1, j + 1)

                return memo[(i, j)]

            # Current character does not match.
            # But current pattern character might have '*' after it.
            if j + 1 < n and p[j + 1] == "*":

                # Use zero occurrences of p[j]
                memo[(i, j)] = dfs(i, j + 2)

                return memo[(i, j)]

            memo[(i, j)] = False
            return False

        return dfs(0, 0)
 
