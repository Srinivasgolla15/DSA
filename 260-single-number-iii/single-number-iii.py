class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)<=2:
            return nums
        xor = 0
        for n in nums:
            xor^=n
        diff = xor&-xor
        a = 0
        b = 0
        for num in nums:
            if num&diff:
                a^=num
            else:
                b^=num
        return [a,b]