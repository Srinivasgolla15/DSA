class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n <= 0:
            return False

        root = int(n ** 0.5)

        if root * root == n and (n & (n - 1)) == 0:
            return (root & (root - 1)) == 0

        return False

        