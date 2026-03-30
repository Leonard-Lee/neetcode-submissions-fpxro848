class Node:
    def __init__(self, key=0, val=0, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next

class LRUCache:

    # hash map + double linked list
    # left: least used
    # right: most used
    def __init__(self, capacity: int):
        self.cap = capacity
        self.mem = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key not in self.mem:
            return -1
        else:
            node = self.mem[key]
            self.remove(node)
            self.insertToTail(node)
            return node.val

    # check if the key exists or not, if so, remove it
    # create a new node with new key/value pair
    # add the node to the dictionary
    # insert the new node to the tail
    # if the dict size exceeds the capability
    # remove the head from dict and linked list
    def put(self, key: int, val: int) -> None:
        if key in self.mem:
            self.remove(self.mem[key])
        node = Node(key, val)
        self.mem[key] = node
        self.insertToTail(node)
        if len(self.mem) > self.cap:
            self.mem.pop(self.head.next.key)
            self.remove(self.head.next)

    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def insertToTail(self, node):
        preTail = self.tail.pre
        preTail.next = node
        node.pre = preTail
        self.tail.pre = node
        node.next = self.tail
        
