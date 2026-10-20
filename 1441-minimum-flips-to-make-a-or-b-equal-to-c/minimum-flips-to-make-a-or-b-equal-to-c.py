class Solution(object):
    def minFlips(self, a, b, c):
        count = 0

        for i in range(32):
            aa = (a >> i) & 1
            bb = (b >> i) & 1
            cc = (c >> i) & 1

            if cc == 1:
                if aa == 0 and bb == 0:
                    count += 1
            else:
                if aa == 1:
                    count += 1
                if bb == 1:
                    count += 1

        return count