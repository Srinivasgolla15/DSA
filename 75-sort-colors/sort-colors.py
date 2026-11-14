class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

# ----------------Counting O(n) O(1)-----------------
        # count0 = 0
        # count1 = 0
        # count2 = 0

        # for num in nums:
        #     if num == 0:
        #         count0 += 1
        #     elif num == 1:
        #         count1 += 1
        #     else:
        #         count2 += 1

        # i = 0

        # while count0 > 0:
        #     nums[i] = 0
        #     i += 1
        #     count0 -= 1

        # while count1 > 0:
        #     nums[i] = 1
        #     i += 1
        #     count1 -= 1

        # while count2 > 0:
        #     nums[i] = 2
        #     i += 1
        #     count2 -= 1


# -----------------TWO PASSES  O(n) O(1)---------
        left = 0

        # Put all 0s at the beginning
        for i in range(len(nums)):

            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1

        # Put all 1s after the 0s
        for i in range(left, len(nums)):

            if nums[i] == 1:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1


        