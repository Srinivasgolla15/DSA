class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

# ----------------BRUTE FORCE --------------------
        # result = 0

        # for left in range(len(nums)):
        #     freq = {}
        #     distinct = 0

        #     for right in range(left, len(nums)):

        #         if nums[right] not in freq:
        #             freq[nums[right]] = 1
        #             distinct += 1
        #         else:
        #             freq[nums[right]] += 1

        #         if distinct == k:
        #             result += 1

        # return result


# Time Complexity: O(N^2)
# Space Complexity: O(N)


# ------------------SLIDING WINDOW + HASHMAP ---------------------------
        
        def find(m):
            left =0
            hm = {}
            count = 0
            for right in range(len(nums)):
                
                if len(hm) <= m :
                    if nums[right] in hm:
                        hm[nums[right]]+=1
                    else: 
                        hm[nums[right]] = 1
                    
                while len(hm) > m:
                    hm[nums[left]]-=1
                    if hm[nums[left]] == 0:
                        del hm[nums[left]]
                    left+=1
                count += right-left+1
                    

            return count
        return find(k)-find(k-1)

                
                


