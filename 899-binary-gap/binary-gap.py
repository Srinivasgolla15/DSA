class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        maxdist = 0
        prev = None
        count=0
        while n:
            r = n%2
            if r==1:
                if prev is not None:
                    maxdist = max(maxdist, count - prev)
                prev = count
            count+=1
            n //= 2
        return maxdist