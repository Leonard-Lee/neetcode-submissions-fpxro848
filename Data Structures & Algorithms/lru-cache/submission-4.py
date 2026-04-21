class Node:
    def __init__(self, key=None, val=None, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head
        
    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.insertToTail(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            self.remove(node)

        newNode = Node(key, value)
        self.map[key] = newNode
        self.insertToTail(newNode)


    def remove(self, node):
        pre = node.pre
        nxt = node.next
        pre.next = nxt
        nxt.pre = pre

    def insertToTail(self, node):
        preTail = self.tail.pre
        preTail.next = node
        node.pre = preTail
        node.next = self.tail
        self.tail.pre = node

        if len(self.map) > self.cap:
            deprecatedNode = self.head.next
            self.remove(deprecatedNode)
            del self.map[deprecatedNode.key]


        
