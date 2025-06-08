# Python List Implementation from Scratch (Dynamic Array Behavior)

import sys
import ctypes

# Python list is a dynamic array. Let's first demonstrate that:
L = []
print("Initial Size:", sys.getsizeof(L))
for i in range(100):
    print(f"Length: {len(L)} | Memory: {sys.getsizeof(L)} bytes")
    L.append(i)

# Now let's create our own custom list class that behaves like a Python list
# We will use ctypes to create low-level arrays (like C-style arrays)

class MyList:
    def __init__(self):
        self.size = 1                     # Total capacity
        self.n = 0                        # Current number of elements
        self.A = self.__make_array(self.size)  # Allocate initial memory

    def __len__(self):
        return self.n

    def __str__(self):
        result = ''
        for i in range(self.n):
            result += str(self.A[i]) + ','
        return '[' + result.rstrip(',') + ']'

    def __getitem__(self, index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            raise IndexError("Index out of range")

    def __delitem__(self, pos):
        if 0 <= pos < self.n:
            for i in range(pos, self.n - 1):
                self.A[i] = self.A[i + 1]
            self.n -= 1
        else:
            raise IndexError("Index out of range")

    def append(self, item):
        if self.n == self.size:
            self.__resize(self.size * 2)
        self.A[self.n] = item
        self.n += 1

    def pop(self):
        if self.n == 0:
            raise IndexError("Pop from empty list")
        popped = self.A[self.n - 1]
        self.n -= 1
        return popped

    def clear(self):
        self.n = 0
        self.size = 1
        self.A = self.__make_array(self.size)

    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return -1  # Item not found

    def remove(self, item):
        pos = self.find(item)
        if pos != -1:
            self.__delitem__(pos)
        else:
            raise ValueError("Item not found")

    def insert(self, pos, item):
        if pos < 0 or pos > self.n:
            raise IndexError("Index out of range")
        if self.n == self.size:
            self.__resize(self.size * 2)
        for i in range(self.n, pos, -1):
            self.A[i] = self.A[i - 1]
        self.A[pos] = item
        self.n += 1

    def __resize(self, new_capacity):
        B = self.__make_array(new_capacity)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.size = new_capacity

    def __make_array(self, capacity):
        # Create a C-style array using ctypes
        return (capacity * ctypes.py_object)()

# Create an instance of the custom list
L = MyList()

# Example usage
L.append(10)
L.append(20)
L.append(30)
print("MyList:", L)
L.insert(1, 15)
print("After Insert:", L)
L.remove(20)
print("After Remove:", L)
print("Pop:", L.pop())
print("Final List:", L)

# Some features to practice:
# - min(), max(), sum()
# - sort()
# - slicing support
# - negative indexing
# - extend() method
# - merging two lists
