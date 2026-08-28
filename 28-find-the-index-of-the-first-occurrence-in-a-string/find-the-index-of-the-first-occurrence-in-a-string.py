class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

# -----------BRUTE FORCE --------------------
        # n =len(needle)
        # i=0
        # k=0
        # if haystack == needle:
        #     return 0
        # while i<=len(haystack)-n:
        #     count = 0
        #     for j in range(i,i+n):        
        #         if haystack[j] == needle[k]:
        #             count+=1
        #         k+=1
        #     if count == n:
        #         return i  
        #     i+=1    
        #     k=0    
        # return -1  
# Time: O((N - M + 1) * M) → O(N * M)
# N = len(haystack), M = len(needle)

# Space: O(1)  


# ---------------SHORTER VERSION OF BRUTEFORCE -----------------
        # for i in range(len(haystack) - len(needle) + 1):
        #     if haystack[i:i + len(needle)] == needle:
        #         return i
        # return -1

# Time: O((N - M + 1) * M) → O(N * M)
# N = len(haystack), M = len(needle)

# Space: O(1) 



# --------------- KMP (Knuth–Morris–Pratt) String Matching using LPS (Longest Prefix Suffix) array --------------------------

        if needle == "":
            return 0

        lps = [0] * len(needle)

        prevLPS, i = 0, 1

        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1

            elif prevLPS == 0:
                lps[i] = 0
                i += 1

            else:
                prevLPS = lps[prevLPS - 1]

        i = 0  # ptr for haystack
        j = 0  # ptr for needle

        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1

            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]

            if j == len(needle):
                return i - len(needle)

        return -1

# Time Complexity: O(N + M)
# N = length of haystack
# M = length of needle
# Building LPS → O(M)
# Searching using KMP → O(N)

# Space Complexity: O(M)
# LPS array stores M elements


