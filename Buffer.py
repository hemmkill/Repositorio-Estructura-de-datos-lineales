class CircularBuffer:
    
    def __init__(self, capacity, initial_elements=None):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0
        if initial_elements:
            for el in initial_elements:
                self.push(el)
    
    def __str__(self):
        elements = list(self)
        return f"CircularBuffer({elements})"
    
    def __len__(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity
    
    def __iter__(self):
        for i in range(self.size):
            yield self.buffer[(self.head + i) % self.capacity]
    
    def __contains__(self, element):
        return any(el == element for el in self)
    
    def push(self, element):
        if self.isFull():
            raise OverflowError("Buffer is full")
        self.buffer[self.tail] = element
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
    
    def pop(self, index=0):
        if self.isEmpty():
            raise IndexError("Buffer is empty")
        real_index = (self.head + index) % self.capacity
        element = self.buffer[real_index]
        if index == 0:
            self.buffer[self.head] = None
            self.head = (self.head + 1) % self.capacity
        else:
            for i in range(index, self.size - 1):
                curr = (self.head + i) % self.capacity
                next_ = (self.head + i + 1) % self.capacity
                self.buffer[curr] = self.buffer[next_]
            self.tail = (self.tail - 1) % self.capacity
            self.buffer[self.tail] = None
        self.size -= 1
        return element
    
    def clear(self):
        self.buffer = [None] * self.capacity
        self.head = 0
        self.tail = 0
        self.size = 0

cb = CircularBuffer(5, [1, 2, 3])
print(cb)          
cb.push(4)
print(3 in cb)     
print(cb.pop(1))   
print(cb)          
cb.clear()
print(cb.isEmpty()) 