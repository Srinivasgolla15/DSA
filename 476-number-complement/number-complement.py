class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        k = 1
        while k<num:
            k= (k<<1)|1
        return k^num