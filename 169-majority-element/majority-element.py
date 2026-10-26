class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for n in nums:
            count[n] = count.get(n,0)+1
        maxi = max(count.values())
        for key,val in count.items():
            if val == maxi:
                return key
        