class Solution(object):
    def findMin(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        low, high = 0, len(arr) - 1

        while low <= high:

            # If current search range is sorted
            if arr[low] <= arr[high]:
                mid = low
                return arr[mid]

            mid = (low + high) // 2

            # Check whether mid is the minimum
            if mid > 0 and arr[mid] < arr[mid - 1]:
                return arr[mid]

            # Minimum is in the right half
            if arr[mid] >= arr[low]:
                low = mid + 1

            # Minimum is in the left half
            else:
                high = mid - 1

        return -1
        # low, high = 0, len(arr) - 1
    
        # while low < high:
        #     mid = (low + high) // 2
            
        #     if arr[mid] > arr[high]:
        #         low = mid + 1
        #     else:
        #         high = mid
        
        # return arr[low]
# time - O(logn) , space - O(1)