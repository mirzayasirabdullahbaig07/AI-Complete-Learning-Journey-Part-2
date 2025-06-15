# What is Linked List in DSA?
# Linked List is very important in DSA.
# Linked List is a linear data structure.
# It is used to store data in non-contiguous memory locations.
# In some cases, it is a replacement for arrays.
# Linked Lists have several benefits.

# How Linked List works:
# Linked List is a collection of nodes.
# Nodes are structures (objects) that store data and the address of the next node.
# The data can be of any type: string, integer, float, etc.

# A node has two parts: 
# - Data
# - Address (reference to the next node)
# The first node is called the head.
# The last node is called the tail — its address points to null.

# Example: 
# First node contains data and the address of the next node (e.g., 700)
# Second node contains its data and address of the third node (e.g., 906), and so on.
# Nodes in Linked Lists are NOT stored in contiguous memory locations.

# Why use Linked List instead of Array?
# Suppose you have an array with 1 lakh elements, and you delete the first item.
# You would have to shift almost 1 lakh items — a very inefficient operation.
# In arrays, deletion or insertion is called a shift operation, which is costly (O(n)).
# Arrays use contiguous memory, while Linked Lists use non-contiguous memory.

# Example use-case: A To-Do List app is a good real-life example of a Linked List.

# In Linked Lists, insertion/deletion is O(1) — you just break and rejoin links.
# Array has fixed size — dynamic arrays solve this to some extent.
# However, dynamic arrays waste a lot of unused memory.
# Example: You create an array of size 4096, and only need to add one more item.
# The array size doubles (~8192), wasting memory.

# Advantages of Linked List:
# - Helps in creating other data structures like:
#   - Stack
#   - Queue
#   - Circular Linked List
#   - Doubly Linked List

# When to use what?
# - Arrays are great for read-heavy operations.
# - Linked Lists are ideal for write-heavy applications.

# Objectives:
# - Create a Linked List  
# - len  
# - Insert from head  
# - Traverse/Print  
# - Insert from tail (append)  
# - Insert in middle (after)  
# - Clear  
# - Delete from head  
# - Delete from tail (pop)  
# - Delete by value (remove)  
# - Search by value (find)  
# - Delete by index → del L[0]  
# - Search by index (indexing)  

# ****************************************

# How to make a class for Node
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

# Creating node objects
a = Node(32)
print(a)
print(a.data)
print(a.next)

# Creating more nodes
b = Node(54)
c = Node(65)

a.next = b
b.next = c

print(a.next)
print(b.next)
print(c.next)

# How to create LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    # Length function
    def __len__(self):
        return self.n

    # Insert from head
    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n += 1

    # Traverse operation
    def traverse(self):
        curr = self.head
        result = ''
        while curr is not None:
            result += str(curr.data) + '->'
            curr = curr.next
        return result[:-2]

    # Insert at tail
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.n += 1
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
        self.n += 1

    # Insert in middle after a given value
    def insert_after(self, after, value):
        new_node = Node(value)
        curr = self.head
        while curr is not None:
            if curr.data == after:
                break
            curr = curr.next
        if curr is not None:
            new_node.next = curr.next
            curr.next = new_node
            self.n += 1
        else:
            return 'Item not found'
        
        # delete using clear
    def clear(self):
        self.head = None
        self.n = 0

        # delete from head
    def delete_head(self):
        if self.head == None:
         # empty

          return 'empty'
        self.head = self.head.next 
        self.n = self.n - 1   
    
    #delete from tail(pop)

    def pop(self):

        curr = self.head
        if self.head == None:
            return "empty list"
        if curr.next == None:
            return self.delete_head()

        while curr.next.next != None:
            curr = curr.next
        # curr secondlast node
        curr.next = None
        self.n = self.n -1 

    def remove_by_value(self, value):
        if self.head == None:
            return "empty list"
        if self.head.data == value:
            # you want to remove the head node
            return self.delete_head()
        curr = self.head

        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next
        
        # item found

        # item not found
        if curr.next == None:
            return "Not Found"
        else:
            curr.next = curr.next.next
        
 # searching in linked list
    def search(self, item):
        curr = self.head
        pos = 0

        while curr != None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos = pos + 1
        return "Not found"
    
    def __getitem__(self, index):
        curr = self.head
        pos = 0

        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos = pos + 1

        return "indexerror"

       

# If you want to reach the last node:       curr != None
# If you want to reach the second last:     curr.next != None
# If you want to stop at third last:        curr.next.next != None

# Create LinkedList object
L = LinkedList()
print(L)

# Linked List key operations:
# - Insert (head, tail, middle)
# - Traverse (print)
# - Delete (tail/pop, value/remove, by index)
# - Search (by value, by index)

# Some common operations:
# - Reverse
# - Find max



# Deletion has 4 cases
# clear mean empty the linked list
# delete freom head
# delete from tail
# delete by value


# now we are moving on searching by value (find)
# delete by index (del)
# search by index (indexing)

# when u use array and linked list

# arrays have fast read operations
# write operation are slow in array


# # linked list have slow read operations
# write operation are fast in linked