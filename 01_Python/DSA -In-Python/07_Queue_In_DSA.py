# --------------------------------------
# Queue in Data Structures (DSA)
# --------------------------------------

# A queue is a linear data structure that follows the **First-In-First-Out (FIFO)** principle.
# The first element inserted is the first one to be removed.

# Structure & Terminology:
# - Insertion happens at the **rear (tail)** — called `enqueue`
# - Deletion happens at the **front (head)** — called `dequeue`

# Queue vs Stack:
# - Stack: Last-In-First-Out (LIFO) → insert & remove from same end.
# - Queue: First-In-First-Out (FIFO) → insert at rear, remove from front.

# Queue operations are performed in **constant time O(1)** for both enqueue and dequeue.

# -------------------------------
# Queue Implementation Using Linked List
# -------------------------------

# Node class to store data and reference to next node
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

# Queue class using linked list
class Queue:
    def __init__(self):
        self.front = None  # Points to the front (head) of queue
        self.rear = None   # Points to the rear (tail) of queue

    # Enqueue: Add element at rear
    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:  # Empty queue
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    # Dequeue: Remove element from front
    def dequeue(self):
        if self.front is None:
            return "Queue is Empty"
        removed = self.front.data
        self.front = self.front.next
        if self.front is None:  # Queue becomes empty after removal
            self.rear = None
        return removed

    # Check if queue is empty
    def is_empty(self):
        return self.front is None

    # Get size of queue
    def size(self):
        count = 0
        temp = self.front
        while temp:
            count += 1
            temp = temp.next
        return count

    # Peek front item
    def front_item(self):
        if self.front is None:
            return "Queue is Empty"
        return self.front.data

    # Peek rear item
    def rear_item(self):
        if self.rear is None:
            return "Queue is Empty"
        return self.rear.data

    # Traverse the queue
    def traverse(self):
        if self.front is None:
            print("Queue is Empty")
            return
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# -------------------------------
# Example Usage
# -------------------------------

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.traverse()              # Output: 10 -> 20 -> 30 -> None

print("Dequeued:", q.dequeue())  # Output: Dequeued: 10
q.traverse()              # Output: 20 -> 30 -> None

print("Front Item:", q.front_item())  # Output: 20
print("Rear Item:", q.rear_item())    # Output: 30
print("Size:", q.size())              # Output: 2
print("Is Empty?", q.is_empty())      # Output: False
