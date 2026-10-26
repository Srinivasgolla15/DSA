class Node(object):
    def __init__(self,val = 0,next = None,prev = None):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList(object):

    def __init__(self):
        self.head = Node()  # Dummy head
        self.tail = Node()  # Dummy tail

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0
        

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        count = 0
        curr = self.head.next
        while count<index:
            curr = curr.next
            count+=1
        return curr.val
         

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        node = Node(val)
        nxt = self.head.next 
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        nxt.prev = node
        
        self.size+=1

    def addAtTail(self, val):
        node = Node(val)
        prev = self.tail.prev

        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

        self.size += 1
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return

        # Find the node currently at this index
        right = self.head.next
        count = 0

        while count < index:
            right = right.next
            count += 1

        # Insert the new node before right
        left = right.prev
        node = Node(val)

        left.next = node
        node.prev = left
        node.next = right
        right.prev = node

        self.size += 1
         
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return

        # Find the node at this index
        curr = self.head.next
        count = 0

        while count < index:
            curr = curr.next
            count += 1

        # Remove curr by connecting its neighbors
        left = curr.prev
        right = curr.next

        left.next = right
        right.prev = left

        self.size -= 1
        
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)