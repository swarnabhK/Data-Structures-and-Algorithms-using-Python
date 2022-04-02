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


def binaryConverter(n,base):
  """Method to convert the base of a number"""
  remstack = Stack()
  while(n>0):
    rem = n%base
    n = n//base
    remstack.push(rem)

  binConverted = ""

  while(not remstack.isEmpty()):
    binConverted+=str(remstack.pop())
  
  return binConverted

  # testing the binaryConverter method.
print(binaryConverter(233))