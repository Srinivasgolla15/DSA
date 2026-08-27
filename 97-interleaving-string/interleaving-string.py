class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
         
         # Total characters must match
        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}

        def dfs(i, j):

            # How many characters of s3 have already been used
            k = i + j

            # All characters have been used
            if k == len(s3):
                return True

            if (i, j) in memo:
                return memo[(i, j)]

            # Take next character from s1
            take_s1 = False

            if i < len(s1) and s1[i] == s3[k]:
                take_s1 = dfs(i + 1, j)

            # Take next character from s2
            take_s2 = False

            if j < len(s2) and s2[j] == s3[k]:
                take_s2 = dfs(i, j + 1)

            # Either choice can successfully form s3
            memo[(i, j)] = take_s1 or take_s2

            return memo[(i, j)]

        return dfs(0, 0)