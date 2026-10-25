# class LRUCache:

#     def __init__(self, capacity):
#         # Time: O(1)
#         # Space: O(capacity)
#         self.capacity = capacity
#         self.cache = []   # Stores (key, value) from LRU -> MRU

#     def get(self, key):
#         """
#         Time Complexity:
#             - Search for key: O(n)
#             - pop(i): O(n)   (elements after i shift left)
#             - append(): O(1)
#             => Overall: O(n)

#         Space Complexity:
#             O(1)
#         """

#         # Search for the key
#         for i in range(len(self.cache)):

#             if self.cache[i][0] == key:

#                 value = self.cache[i][1]

#                 # Remove the key from its current position
#                 # Time: O(n)
#                 self.cache.pop(i)

#                 # Move it to the end (Most Recently Used)
#                 # Time: O(1)
#                 self.cache.append((key, value))

#                 return value

#         # Key not found
#         return -1

#     def put(self, key, value):
#         """
#         Time Complexity:
#             - Search for existing key: O(n)
#             - pop(i): O(n)
#             - pop(0): O(n)
#             - append(): O(1)
#             => Overall: O(n)

#         Space Complexity:
#             O(1) extra
#         """

#         # Check if the key already exists
#         for i in range(len(self.cache)):

#             if self.cache[i][0] == key:

#                 # Remove old entry
#                 # Time: O(n)
#                 self.cache.pop(i)

#                 # Reinsert at the end (Most Recently Used)
#                 # Time: O(1)
#                 self.cache.append((key, value))

#                 return

#         # Cache is full
#         if len(self.cache) == self.capacity:

#             # Remove the Least Recently Used item
#             # pop(0) shifts every remaining element
#             # Time: O(n)
#             self.cache.pop(0)

#         # Insert the new item at the end (Most Recently Used)
#         # Time: O(1)
#         self.cache.append((key, value))


# ----------------OPTIMIZED WAY Hashmap+DLL---------------------
# class Node:
#     """
#     Doubly Linked List Node

#     Stores:
#         key
#         value
#         prev pointer
#         next pointer
#     """

#     def __init__(self, key=0, value=0):
#         self.key = key
#         self.value = value

#         self.prev = None
#         self.next = None


# class LRUCache:

    # def __init__(self, capacity):
    #     """
    #     Time: O(1)
    #     Space: O(capacity)
    #     """

    #     self.capacity = capacity

    #     # Dictionary:
    #     # key -> corresponding DLL node
    #     self.cache = {}

    #     # Dummy Head (LRU side)
    #     self.head = Node()

    #     # Dummy Tail (MRU side)
    #     self.tail = Node()

    #     # Connect dummy nodes
    #     self.head.next = self.tail
    #     self.tail.prev = self.head

    # ########################################################
    # # Remove a node from the linked list
    # ########################################################
    # def remove(self, node):
    #     """
    #     Time: O(1)
    #     Space: O(1)
    #     """

    #     prev_node = node.prev
    #     next_node = node.next

    #     prev_node.next = next_node
    #     next_node.prev = prev_node

    # ########################################################
    # # Insert a node before the dummy tail
    # # (Most Recently Used Position)
    # ########################################################
    # def insert(self, node):
    #     """
    #     Time: O(1)
    #     Space: O(1)
    #     """

    #     prev_node = self.tail.prev

    #     prev_node.next = node
    #     node.prev = prev_node

    #     node.next = self.tail
    #     self.tail.prev = node

    # ########################################################
    # # GET
    # ########################################################
    # def get(self, key):
    #     """
    #     Time: O(1)
    #     Space: O(1)
    #     """

    #     # Key doesn't exist
    #     if key not in self.cache:
    #         return -1

    #     node = self.cache[key]

    #     # Move node to MRU position
    #     self.remove(node)
    #     self.insert(node)

    #     return node.value

    # ########################################################
    # # PUT
    # ########################################################
    # def put(self, key, value):
    #     """
    #     Time: O(1)
    #     Space: O(1)
    #     """

    #     # Key already exists
    #     if key in self.cache:

    #         node = self.cache[key]
 
    #         # Update value
    #         node.value = value

    #         # Move to MRU
    #         self.remove(node)
    #         self.insert(node)

    #         return

    #     ####################################################
    #     # New key
    #     ####################################################

    #     node = Node(key, value)

    #     self.cache[key] = node

    #     self.insert(node)

    #     ####################################################
    #     # Cache exceeds capacity
    #     ####################################################

    #     if len(self.cache) > self.capacity:

    #         # LRU node = first real node
    #         lru = self.head.next

    #         # Remove from linked list
    #         self.remove(lru)

    #         # Remove from dictionary
    #         del self.cache[lru.key]



from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1

        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

