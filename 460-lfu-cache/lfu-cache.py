class Node(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DLL(object):

    def __init__(self):
        # Dummy nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        # Insert at the end = most recently used
        prev_node = self.tail.prev

        prev_node.next = node
        node.prev = prev_node

        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node


class LFUCache(object):

    def __init__(self, capacity):
        self.cache = {}       # key -> Node
        self.freq_map = {}    # frequency -> DLL
        self.cap = capacity
        self.min_freq = 0

    def get_dll(self, freq):
        if freq not in self.freq_map:
            self.freq_map[freq] = DLL()

        return self.freq_map[freq]

    def increase_freq(self, node):
        old_freq = node.freq

        # Remove from old frequency DLL
        old_dll = self.freq_map[old_freq]
        old_dll.remove(node)

        # If this was the last node with minimum frequency
        if old_freq == self.min_freq:
            if old_dll.head.next == old_dll.tail:
                self.min_freq += 1

        # Increase node frequency
        node.freq += 1

        # Put node into new frequency DLL
        new_dll = self.get_dll(node.freq)
        new_dll.insert(node)

    def get(self, key):

        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.increase_freq(node)

        return node.value

    def put(self, key, value):

        if self.cap == 0:
            return

        # Existing key
        if key in self.cache:

            node = self.cache[key]

            node.value = value

            self.increase_freq(node)

            return

        # Cache is full -> remove LFU node
        if len(self.cache) >= self.cap:

            min_dll = self.freq_map[self.min_freq]

            # First node after head = LRU among minimum frequency
            node_to_remove = min_dll.head.next

            min_dll.remove(node_to_remove)

            del self.cache[node_to_remove.key]

        # New node always starts with frequency 1
        node = Node(key, value)

        self.cache[key] = node

        dll = self.get_dll(1)
        dll.insert(node)

        self.min_freq = 1