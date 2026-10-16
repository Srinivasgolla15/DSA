class Solution(object):
    def countBits(self, n):
# ---------------BRUTE FORCE ---------------
        # """
        # Time Complexity: O(n log n)
        # - We iterate through all numbers from 0 to n.
        # - Counting set bits for one number takes O(log n) in the worst case.
        # - Total: O(n log n)

        # Space Complexity: O(1)
        # - Ignoring the output array.
        # - Only a few extra variables are used.
        # """

        # ans = []

        # for i in range(n + 1):

        #     num = i
        #     count = 0

        #     while num:
        #         count += num & 1
        #         num >>= 1

        #     ans.append(count)

        # return ans

        def dfs(num):
            count = 0
            while num:
                num&=(num-1)
                count+=1
            return count
        arr = [0]*(n+1)
        for num in range(n+1):
            counts = dfs(num)
            arr[num]=counts
        return arr

# -------------------DP using Right Shif--------------------
        """
        Time Complexity: O(n)
        - Each number is processed exactly once.

        Space Complexity: O(n)
        - DP array of size n + 1.
        """

        # dp = [0] * (n + 1)

        # for i in range(1, n + 1):
        #     dp[i] = dp[i >> 1] + (i & 1)

        #     # think of  i>>1 as i//2  and i&1 is last bit checking as i%2

        # return dp

# -------------------- USING DP as same but different  idea logy -----------

        # dp = [0] * (n + 1)

        # for i in range(1, n + 1):
        #     dp[i] = dp[i // 2] + (i % 2)  
            

        # return dp

# -------------------DP using Brian Kernighan ----------------

        """
        Time Complexity: O(n)

        Space Complexity: O(n)
        """

        # dp = [0] * (n + 1)

        # for i in range(1, n + 1):
        #     dp[i] = dp[i & (i - 1)] + 1

        # return dp