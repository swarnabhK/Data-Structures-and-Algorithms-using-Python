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


def par_checker(expr):

  """if opening parantheses, push in a stack.
  If closing parantheses, compare the opening parantheses at the top of the stack,
  if parantheses are of matching type, pop the opening parantheses from the stack."""

  a = Stack()
  par_dict = {')':'(','}':'{',']':'['}
  for i in expr:
    if(i in '({['):
      a.push(i)
    elif(i in ')}]'):
      if(a.isEmpty() or a.peek()!=par_dict[i]):
        return False
      else:
        a.pop()
  return a.stack_size()==0

# testing the par checker method.
print("Testing the par_checker method.")
print(par_checker('{()()}'))
print(par_checker('((()))'))
print(par_checker('(()'))
print(par_checker('{({([][])}())}'))
print(par_checker('[{()]'))


