class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n =len(needle)
        i=0
        k=0
     
        if haystack == needle:
            return 0
        while i<=len(haystack)-n:
            count = 0
            for j in range(i,i+n):        
                if haystack[j] == needle[k]:
                    count+=1
                k+=1
            if count == n:
                return i  
            i+=1    
            k=0    
           
   
        return -1    
