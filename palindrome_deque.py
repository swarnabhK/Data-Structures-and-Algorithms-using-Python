class Deque:
  def __init__(self):
    self.items=[]
  def isEmpty(self):
    return self.items == []
  def addFront(self,item):
    self.items.insert(0,item)
  def removeFront(self):
    return self.items.pop(0)
  def addRear(self,item):
    self.items.append(item)
  def removeRear(self):
    return self.items.pop()
  def deque_size(self):
    return len(self.items)

def isPalindrome(str):
  """Removing the rear and front characters directly and comparing them to see if they are equal."""
  d = Deque()
  for s in str:
    d.addFront(s)
  stillEqual = True
  while(d.deque_size()>1 and stillEqual):
    first = d.removeFront()
    end = d.removeRear()
    if(first!=end):
      stillEqual = False
  return stillEqual


print(isPalindrome("lsdkjfskf"))
print(isPalindrome("radar"))