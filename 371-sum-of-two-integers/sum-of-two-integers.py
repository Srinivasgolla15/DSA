class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        carry = 0
        num = 0

        for i in range(32):
            x = (a >> i) & 1
            y = (b >> i) & 1

            p = x ^ y ^ carry
            num |= p << i

            carry = (x & y) | (carry & (x ^ y))

        if num>0x7FFFFFFF:
            num=~(num^0xFFFFFFFF)

        return num