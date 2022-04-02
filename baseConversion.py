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


def baseConverter(n,base):
  """Method to convert the base of a number"""
  remstack = Stack()
  digits = "0123456789ABCDEF" #for representing digits beyond base 10
  
  while(n>0):
    rem = n%base
    n = n//base
    remstack.push(rem)

  baseConverted = ""

  while(not remstack.isEmpty()):
    baseConverted+=digits[remstack.pop()]
  
  return baseConverted

  # testing the binaryConverter method.
print(baseConverter(233,2))
print(baseConverter(25,8))
print(baseConverter(256,16))
print(baseConverter(26,26))