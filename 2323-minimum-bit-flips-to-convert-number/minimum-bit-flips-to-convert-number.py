class Solution(object):
    def minBitFlips(self, start, goal):
        # count = 0

        # for i in range(32):
        #     a = (goal >> i) & 1
        #     b = (start >> i) & 1

        #     if a != b:
        #         count += 1

        # return count


        count = 0

        for i in range(32):
            a = goal & (1 << i)
            b = start & (1 << i)

            if a != b:
                count += 1

        return count