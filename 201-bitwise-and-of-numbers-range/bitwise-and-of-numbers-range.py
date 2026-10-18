class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == right:
            return left&right
        for i in range(32):
            left = left>>1 
            right = right>>1

            if left == right:
                return left<<(i+1)
        

        