class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # num = 0
        # stack = []
        # for i in range(32):
        #     stack.append(n % 2)
        #     n //= 2
        # for i in range(32):
        #     num += stack.pop() * (2 ** i)
        # return num

        result = 0
        for i in range(32):  # 32-bit integer
            # Shift result left to make room
            result <<= 1
            # Add the least significant bit of n
            result |= (n & 1)
            # Shift n right to process next bit
            n >>= 1
        return result