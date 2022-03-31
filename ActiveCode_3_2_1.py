import time

def sumOfN(n):
  """A basic sum of n number function"""
  theSum = 0
  for i in range(1,n+1):
    theSum+=i
  return theSum

def sumOfN2(n):
  """A sum function which keeps track of the start and end of the execution
  time"""
  start = time.time()
  theSum = 0
  for i in range(1,n+1):
    theSum+=i
  end = time.time()
  return theSum,end-start

for i in range(5):
  print("Sum is %d, it required %10.7f seconds"%sumOfN2(10000))