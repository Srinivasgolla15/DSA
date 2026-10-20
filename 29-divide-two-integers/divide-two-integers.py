class Solution(object):
    def divide(self, dividend, divisor):
        d = abs(dividend)
        n = abs(divisor)
        res = 0

        while d >= n:
            i = 0
            while (n << (i )) <= d:
                i += 1

            d -= n << (i-1)
            res += 1 << (i-1)

        if (dividend < 0) != (divisor < 0):
            res = -res

        if res > 0x7FFFFFFF:
            return 0x7FFFFFFF
        if res < -0x80000000:
            return -0x80000000

        return res