class Node:
    def __init__(self, key=0, val=0, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        # map a key to a node
        self.mapping = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1

        node = self.mapping[key]
        self.remove(node)
        self.insertToTail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.remove(self.mapping[key])

        newNode = Node(key, value)
        self.mapping[key] = newNode
        self.insertToTail(newNode)

    def remove(self, node: Node) -> None:
        pre = node.pre
        nxt = node.next
        pre.next = nxt
        nxt.pre = pre

        node.pre = None
        node.next = None
        
    def insertToTail(self, node: Node) -> None:
        preTail = self.tail.pre
        preTail.next = node
        node.pre = preTail
        self.tail.pre = node
        node.next = self.tail

        if len(self.mapping) > self.cap:
            deletedNode = self.head.next
            self.remove(deletedNode)
            del self.mapping[deletedNode.key]
