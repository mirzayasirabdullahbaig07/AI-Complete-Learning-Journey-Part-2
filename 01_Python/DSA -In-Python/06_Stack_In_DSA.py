# What is stack?
# stack is the data structure which is used to store data
# it is similar to linked list. it use the simple called LIFO
# Last In first Out
# Stacks are very useful and important fuctions
# You can make stack using arrays as well using linked Lists
# stack have on top where u push items or data
# pop is the other operation
# peak is the top most item of the stack
# is_empty it tells the stack is empty or not
# size - tells the number of items in stack

# if all working on top using linked list the last item is pointing towards none
class Node:
  def __init__(self, value):
    self.data = value
    self.none = None

class Stack:
  def __init__(self):
    self.top = None
  def isempty(self):
    return self.top == None

  def push(self, value):
    new_node = Node(value)
    new_node.next = self.top
    self.top = new_node
  
  def peek(self):
    if(self.isempty()):
      return "Stack Empty"
    else:
      return self.top.data
  
def pop(self):
  if(self.isempty()):
    return "Stack Empty"
  else:
    self.top = self.top.next

  def traverse(self):
    temp = self.top
    while temp != None:
      print(temp.data)
      temp = temp.next

s = Stack()
s.isempty()

s.push(2)
s.isempty()

s.push(3)
s.push(4)
s.push(5)

s.traverse()
s.peek()


# Now using arrays to make stacks

class Stack:
  def __init__(self, size):
    self.size = size
    self.stack = [None] * self.size
    self.top = -1
  def push(self, value):
   if self.top == self.size - 1:
     return "Overflow"
   else:
     self.top += 1
     self.stack[self.top] = value
  
  def pop(self):
    if self.top == -1:
      return "empty"
    else:
      data = self.stack[self.top]
      self.top-= 1
      print(data)
  def traverse(self):
    for i in range(self.temp + 1):
      print(self.stack[i], end = ' ')
 