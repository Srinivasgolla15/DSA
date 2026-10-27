
class Solution(object):
    def maxSubarraySumCircular(self, nums):
        total = sum(nums)

        curr_max = max_sum = nums[0]
        curr_min = min_sum = nums[0]

        for i in range(1, len(nums)):
            curr_max = max(nums[i], curr_max + nums[i])
            max_sum = max(max_sum, curr_max)

            curr_min = min(nums[i], curr_min + nums[i])
            min_sum = min(min_sum, curr_min)

        # All numbers are negative: don't choose an empty subarray
        if max_sum < 0:
            return max_sum

        # Compare normal and circular maximum sums
        return max(max_sum, total - min_sum)
