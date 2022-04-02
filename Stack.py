class Stack:

  """Implementation of the stack data structure."""
  def __init__(self):
    self.items = []

  def push(self,item):
    self.items.append(item)

  def isEmpty(self):
    return self.items==[]
    
  def pop(self):
    return self.items.pop()

  def peek(self):
    return self.items[len(self.items)-1]

  def stack_size(self):
    return len(self.items)
  

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