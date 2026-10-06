class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

# #  --------------TWO LOOPS DP O(n^2) O(n)----------------------
#         n = len(nums)

#         if n == 0:
#             return 0

#         dp = [1] * n

#         for i in range(n):
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     dp[i] = max(dp[i], dp[j] + 1)

#         return max(dp)

# ----------------------RECURSION O(2^n) O(n)-----------------------------
        # def rec(i, prev):
        #     if i == len(nums):
        #         return 0

        #     take = 0

        #     if prev == -1 or nums[i] > nums[prev]:
        #         take = 1 + rec(i + 1, i)

        #     skip = rec(i + 1, prev)

        #     return max(take, skip)

        # return rec(0, -1)

# -------------------------MEMOIZATION O(n^2) O(n^2)---------------------
        # memo = {}

        # def rec(i, prev):
        #     if i == len(nums):
        #         return 0

        #     if (i, prev) in memo:
        #         return memo[(i, prev)]

        #     take = 0

        #     if prev == -1 or nums[i] > nums[prev]:
        #         take = 1 + rec(i + 1, i)

        #     skip = rec(i + 1, prev)

        #     memo[(i, prev)] = max(take, skip)

        #     return memo[(i, prev)]

        # return rec(0, -1)


# ---------------BINARY SEARCH O(NlogN) O(n)-------------------
        lis = []
        for num in nums:
            left = 0
            right = len(lis)

            while left<right:
                mid = (left+right)//2
                if lis[mid]<num:
                    left=mid+1
                else:
                    right = mid
            if left!=len(lis):
                lis[left] = num
            else:
                lis.append(num)
        return len(lis)