class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

# ------------------BRUTE FORCE -----------------------
# Time:  O(n²)
# Space: O(n)

        # # Start from the end of the string
        # i = len(s) - 1

        # # Find the longest palindromic prefix
        # while i >= 0:

        #     # Check whether s[0:i+1] is a palindrome
        #     if s[:i + 1] == s[:i + 1][::-1]:
        #         break

        #     i -= 1

        # # Everything after the palindromic prefix
        # remaining = s[i + 1:]

        # # Reverse the remaining part and add it in front
        # return remaining[::-1] + s


        if s == s[::-1]:
            return s
        string = s + "#" + s[::-1]
        lps = [0]*len(string)
        prevLPS,i=0,1
        while i<len(string):
            if string[prevLPS] == string[i]:
                lps[i] = prevLPS+1
                prevLPS+=1
                i+=1
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS-1]
        
        l = lps[-1]
        return s[l:][::-1]+s


