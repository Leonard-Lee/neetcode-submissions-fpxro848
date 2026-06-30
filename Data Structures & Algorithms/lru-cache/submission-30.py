class ListNode:
    def __init__(self, key=0, val=0, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        # map a key to a double linked list node
        self.map = {}
        self.cap = capacity

        # oldest -> youngest
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]
        self.remove(node)
        self.insertToTail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])

        newNode = ListNode(key, value)
        self.map[key] = newNode
        self.insertToTail(newNode)

    def remove(self, node: ListNode) -> None:
        pre = node.pre
        nxt = node.next

        pre.next = nxt
        nxt.pre = pre

        node.pre = None
        node.next = None

    def insertToTail(self, node: ListNode) -> None:
        preTail = self.tail.pre
        preTail.next = node
        node.pre = preTail
        self.tail.pre = node
        node.next = self.tail

        if len(self.map) > self.cap:
            firstNode = self.head.next
            self.remove(firstNode)
            del self.map[firstNode.key]
        
