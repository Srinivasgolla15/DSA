# class Solution(object):
#     def findMaximumXOR(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """

# ----------------Brute Force  (TLE)------------------
        # max_xor = 0

        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         max_xor = max(max_xor, nums[i] ^ nums[j])

        # return max_xor

# Time: O(n^2)
# Space: O(1)


# ---------------trie O(32n) 

# class TrieNode(object):
#     def __init__(self):
#         self.child = {}


# class Solution(object):
#     def findMaximumXOR(self, nums):
#         root = TrieNode()

#         # Step 1: Insert all numbers into the binary Trie
#         for num in nums:
#             node = root

#             for i in range(31, -1, -1):
#                 bit = (num >> i) & 1

#                 if bit not in node.child:
#                     node.child[bit] = TrieNode()

#                 node = node.child[bit]

#         # Step 2: Find the maximum XOR for each number
#         res = 0

#         for num in nums:
#             node = root
#             cur_xor = 0

#             for i in range(31, -1, -1):
#                 bit = (num >> i) & 1
#                 opposite = 1 - bit

#                 if opposite in node.child:
#                     cur_xor |= (1 << i)
#                     node = node.child[opposite]
#                 else:
#                     node = node.child[bit]

#             res = max(res, cur_xor)

#         return res

# --------------31n --------------
# class TrieNode(object):
#     def __init__(self):
#         self.child = [None, None]


# class Solution(object):
#     def findMaximumXOR(self, nums):
#         root = TrieNode()

#         # Insert every number
#         for num in nums:
#             node = root

#             for i in range(30, -1, -1):
#                 bit = (num >> i) & 1

#                 if node.child[bit] is None:
#                     node.child[bit] = TrieNode()

#                 node = node.child[bit]

#         # Query every number
#         res = 0

#         for num in nums:
#             node = root
#             cur_xor = 0

#             for i in range(30, -1, -1):
#                 bit = (num >> i) & 1
#                 opposite = 1 - bit

#                 if node.child[opposite] is not None:
#                     cur_xor |= (1 << i)
#                     node = node.child[opposite]
#                 else:
#                     node = node.child[bit]

#             res = max(res, cur_xor)

#         return res


class Solution:
    def findMaximumXOR(self, nums):
        ans, mask = 0, 0
        for i in range(31, -1, -1):
            mask |= 1<<i
            found = set([num & mask for num in nums])
                
            start = ans | 1<<i
            for pref in found:
                if start^pref in found:
                    ans = start
                    break
         
        return ans