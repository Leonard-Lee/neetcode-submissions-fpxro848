class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        # head: least recently used
        # tail: most recently used
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.pre = self.tail, self.head
        self.cache = {}

    def remove(self, node):
        pre, nxt = node.pre, node.next
        pre.next = nxt
        nxt.pre = pre

    # most recently used
    def insertToTail(self, node):
        pre = self.tail.pre
        pre.next = node
        node.pre = pre
        self.tail.pre = node
        node.next= self.tail


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insertToTail(node)
            return node.val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        newNode = Node(key, value)
        self.cache[key]= newNode
        self.insertToTail(newNode)

        # if it exceeds its capacity
        if len(self.cache) > self.cap:
            # remove the head LSU
            removedNode = self.head.next
            self.remove(removedNode)
            del self.cache[removedNode.key]


        
