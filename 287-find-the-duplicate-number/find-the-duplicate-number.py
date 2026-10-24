class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dup = set()
        for i in nums:
            if i in dup:
                return i
            dup.add(i)
            
        