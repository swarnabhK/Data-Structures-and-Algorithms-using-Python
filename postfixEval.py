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


def postfixEval(pos):
  operandStack = Stack()
  pos = pos.split()

  for i in pos:
    if(i in "0123456789"):
      operandStack.push(i)
    else:
      op2 = operandStack.pop()
      op1 = operandStack.pop()
      operandStack.push(doMath(i,int(op1),int(op2)))
  return operandStack.pop()

def doMath(i,op1,op2):
  if(i=="*"):
    return op1*op2
  elif(i=="/"):
    return op1//op2
  elif(i=="+"):
    return op1+op2
  else:
    return op1-op2

print(postfixEval('7 8 + 3 2 + /'))