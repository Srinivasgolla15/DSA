class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        arr = [0]*(n+1)
        arr[1] = 1
        arr[2] = 2
        for i in range(3,n+1):
            arr[i] = arr[i-1]+arr[i-2]
        return arr[n]
        # this recursion makes longer time limits
        # def ways(num):
        #     if num==1:
        #         return 1 
        #     elif num == 2:
        #         return 2
        #     return ways(num-1)+ways(num-2)
        # return ways(n)
    # ------> time O(2^n ) space (recursive callstack) O(n)---------
# dynamic programming version 
        # if n <= 2:
        #     return n

        # dp = [0] * (n + 1)

        # dp[1] = 1
        # dp[2] = 2

        # for i in range(3, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]

        # return dp[n]

        # # time and space is O(n)


        

        