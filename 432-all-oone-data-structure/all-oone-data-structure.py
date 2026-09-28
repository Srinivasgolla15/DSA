# class AllOne(object):

#     def __init__(self):
#         self.hm = {}
#         self.freq = {}

#     def inc(self, key):
#         """
#         :type key: str
#         :rtype: None
#         """
#         old = self.hm.get(key,0)
#         if old > 0:
#             self.freq[old].remove(key)
#             if not self.freq[old]:
#                 del self.freq[old]

#         self.hm[key] = self.hm.get(key,0)+1
#         value = self.hm[key]
#         if value in self.freq:
#             self.freq[value].append(key)
#         else:
#             self.freq[value] = [key]
        

#     def dec(self, key):
#         """
#         :type key: str
#         :rtype: None
#         """
#         old = self.hm[key]

#         self.freq[old].remove(key)

#         if not self.freq[old]:
#             del self.freq[old]

#         new = old - 1

#         if new == 0:
#             del self.hm[key]
#         else:
#             self.hm[key] = new

#             if new not in self.freq:
#                 self.freq[new] = []

#             self.freq[new].append(key)
        

#     def getMaxKey(self):
#         """
#         :rtype: str
#         """
#         if not self.freq:
#             return ""
#         maxi = max(self.freq.keys())
#         return self.freq[maxi][0]
        

#     def getMinKey(self):
#         """
#         :rtype: str
#         """
#         if not self.freq:
#             return ""
#         mini = min(self.freq.keys())
#         return self.freq[mini][0]
        

# ------------------DLL approach ------------------------

class Node(object):

    def __init__(self, freq):
        self.freq = freq
        self.keys = set()

        self.prev = None
        self.next = None


class AllOne(object):

    def __init__(self):
        # key -> Node
        self.hm = {}

        # DLL of frequency buckets
        self.head = Node(0)
        self.tail = Node(0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_after(self, prev_node, node):
        next_node = prev_node.next

        prev_node.next = node
        node.prev = prev_node

        node.next = next_node
        next_node.prev = node

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def inc(self, key):
        if key not in self.hm:
            # New key -> frequency 1

            # If first bucket is not freq 1, create it
            if self.head.next == self.tail or self.head.next.freq != 1:
                node = Node(1)
                self.insert_after(self.head, node)
            else:
                node = self.head.next

            node.keys.add(key)
            self.hm[key] = node

        else:
            # Existing key
            old_node = self.hm[key]
            old_freq = old_node.freq
            new_freq = old_freq + 1

            # Check whether next bucket is already new_freq
            if old_node.next == self.tail or old_node.next.freq != new_freq:
                new_node = Node(new_freq)
                self.insert_after(old_node, new_node)
            else:
                new_node = old_node.next

            # Move key
            old_node.keys.remove(key)
            new_node.keys.add(key)

            self.hm[key] = new_node

            # Remove empty old bucket
            if len(old_node.keys) == 0:
                self.remove(old_node)

    def dec(self, key):
        old_node = self.hm[key]
        old_freq = old_node.freq
        new_freq = old_freq - 1

        # Frequency becomes 0
        if new_freq == 0:
            old_node.keys.remove(key)
            del self.hm[key]

            if len(old_node.keys) == 0:
                self.remove(old_node)

            return

        # Check whether previous bucket is already new_freq
        if old_node.prev == self.head or old_node.prev.freq != new_freq:
            new_node = Node(new_freq)
            self.insert_after(old_node.prev, new_node)
        else:
            new_node = old_node.prev

        # Move key
        old_node.keys.remove(key)
        new_node.keys.add(key)

        self.hm[key] = new_node

        # Remove empty old bucket
        if len(old_node.keys) == 0:
            self.remove(old_node)

    def getMaxKey(self):
        if self.tail.prev == self.head:
            return ""

        node = self.tail.prev

        return next(iter(node.keys))

    def getMinKey(self):
        if self.head.next == self.tail:
            return ""

        node = self.head.next

        return next(iter(node.keys))
 