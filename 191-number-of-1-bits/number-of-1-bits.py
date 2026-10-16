class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
# ------------------BRUTE FORCE O(log n) O(1)-----------------
        # count =0 
        # while n:
        #     if n % 2 !=0:
        #         count+=1
        #     n=n//2
        # return count

# -----------------Bitwise (&1, >>1) O(log n) O(1)-------------------
        # count = 0

        # while n:
        #     count += n & 1
        #     n >>= 1

        # return count

# ---------------Brian Kernighan O(number of set bits) O(1)------------
        count = 0

        while n:
            n&=(n-1)
            count+=1
        
        return count



        