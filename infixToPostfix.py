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

def PostfixConverter(inf):
  """A method to convert an infix expression into postfix expression.
  a) Check for whether it's an operand or a operator.
  b) If operand, append it into a list
  c) If operator , check whether there are other operators with higher precedence present in the operand stack. If present pop all those operators out from the stack and finally push the current operator into the opstack."""

  prec_dict = {"*":3,"/":3,"+":2,"-":2,"(":1}
  opstack = Stack()
  output = []
  inf = inf.split()
  for i in inf:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or i in "0123456789":
      output.append(i)
    elif i =="(":
      opstack.push(i)
    elif i==")":
      topToken = opstack.pop()
      while topToken != '(':
        output.append(topToken)
        topToken = opstack.pop()
    else:
      while(not opstack.isEmpty() and (prec_dict[opstack.peek()]>=prec_dict[i])):
        output.append(opstack.pop())
      opstack.push(i)
  while(not opstack.isEmpty()):
    output.append(opstack.pop())
  return " ".join(output)


print(PostfixConverter("A * B + C * D"))
print(PostfixConverter("( A + B ) * C - ( D - E ) * ( F + G )"))