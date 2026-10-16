class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
# ---------------bit manipulation
        sol = 0
        n = len(nums)
        # expected
        for i in range(n + 1):
            sol ^= i
        # actual
        for num in nums:
            sol ^= num

        return sol

# ----------brute force O(n2)--------------
        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         return i

# ------------sum formula O(n)------------
        # n = len(nums)
        # expected = n * (n + 1) // 2
        # actual = sum(nums)

        # return expected - actual

        