class Solution(object):

    def findKthLargest(self, nums, k):

        sorted_arr = sorted(nums)
        length = len(sorted_arr)
        largest = sorted_arr[length - k]

        return largest

        heap = []
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]
        
        