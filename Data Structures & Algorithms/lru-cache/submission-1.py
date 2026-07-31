class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}  # hashmap key → node
        
        self.left = Node(0, 0)   # LRU dummy
        self.right = Node(0, 0)  # MRU dummy
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        # remove a node from linked list
        # hint: connect node's prev and next to each other
        prv = node.prev
        nxt = node.next
        prv.next = nxt
        nxt.prev = prv
    
    def insert(self, node):
        # insert node right before RIGHT
        # hint: you need to update 4 pointers
        prv = self.right.prev
        prv.next = node
        node.prev = prv
        node.next = self.right
        self.right.prev = node
    
    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])   # remove from current position
            self.insert(self.cache[key])   # reinsert as MRU ← missing!
            return self.cache[key].val
        return -1
    
    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node
        if len(self.cache) > self.cap:
            lru = self.left.next        # node right after LEFT = LRU
            self.remove(lru)
            del self.cache[lru.key]
        