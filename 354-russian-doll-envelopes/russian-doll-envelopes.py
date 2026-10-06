class Solution(object):
    def maxEnvelopes(self, envelopes):
        
#         # Sort width ascending; same width -> height descending
#         envelopes.sort(key=lambda x: (x[0], -x[1]))

#         # LIS starts here: we will find LIS on heights
#         tails = []

#         for arr in envelopes:
#             height = arr[1]

#             # Find first position where tails[pos] >= height
#             left = 0
#             right = len(tails)

#             while left < right:
#                 mid = (left + right) // 2

#                 if tails[mid] < height:
#                     left = mid + 1
#                 else:
#                     right = mid

#             # No bigger/equal value -> extend LIS
#             if left == len(tails):
#                 tails.append(height)
#             else:
#                 # Replace with smaller ending value
#                 tails[left] = height

#         return len(tails)


# # Time Complexity: O(N log N)
# # Space Complexity: O(N)


        import bisect

        if not envelopes:
            return 0

        # Width ascending, height descending for equal widths
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        lis = []

        for w, h in envelopes:
            pos = bisect.bisect_left(lis, h)

            if pos == len(lis):
                lis.append(h)
            else:
                lis[pos] = h

        return len(lis)