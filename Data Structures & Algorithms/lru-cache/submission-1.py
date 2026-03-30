class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next, self.tail.pre = self.tail, self.head

    def remove(self, node):
        pre, nxt = node.pre, node.next
        pre.next = nxt
        nxt.pre = pre
    
    def insertTail(self, node):
        oldPreTail = self.tail.pre
        oldPreTail.next = node
        node.pre = oldPreTail
        node.next = self.tail
        self.tail.pre = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insertTail(node)
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = Node(key, value)
        self.insertTail(node)
        self.cache[key] = node
        
        # remove from head LRU
        if len(self.cache) > self.cap:
            preHead = self.head.next
            del self.cache[preHead.key]
            self.remove(preHead)

        
