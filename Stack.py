class Stack:
  
  """Implementation of the stack data structure."""
  def __init__(self):
    self.items = []
    self.size = 0

  def push(self,item):
    self.items.append(item)
    self.size+=1

  def pop(self):

    popped_item = self.items[self.size-1]
    self.size-=1
    return popped_item

  def peek(self):
    return self.items[self.size-1]

  def stack_size(self):
    return self.size
  

# testing the stack data structure.
s = Stack()
s.push(1)
s.push("Hola")
s.push("!")
s.push(23)
s.push("Kela")
print(s.pop())
print(s.peek())
print(s.stack_size())