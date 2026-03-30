class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

class LRUCache:

    # We are going to leverage a double linked list and hash table
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        # Least Recent Use
        self.head = ListNode(0, 0)
        # Most Recent Use
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head
        
    def remove(self, node):
        pre, nxt = node.pre, node.next
        if pre: pre.next = nxt
        nxt.pre = pre

    def insertTail(self, node):
        oldTail = self.tail.pre
        oldTail.next = node
        node.pre = oldTail
        node.next = self.tail
        self.tail.pre = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insertTail(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = ListNode(key, value)
        self.insertTail(node)
        self.cache[key] = node

        if len(self.cache) > self.cap:
            # remove from the head
            deleted = self.head.next
            print("deleted key: " + str(deleted.key))
            self.remove(deleted)
            del self.cache[deleted.key]

        
