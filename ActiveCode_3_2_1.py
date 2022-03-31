import time

# Key takeaway: he benchmark technique computes the actual time to execute. It does # not really provide us with a useful measurement, because it is dependent on a #particular machine, program, time of day, compiler, and programming language.


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

def sumofN3(n):
  """This function is based on the summation problem."""
  start = time.time()
  sum = (n*(n+1))/2
  end = time.time()
  return sum, end-start

for i in range(5):
  """Running benchmark tests for values of n=10000,100000,1000000 using the sumOfN2 function"""
  print("Sum is %d, it required %10.7f seconds"%sumOfN2(10000))
  print("Sum is %d, it required %10.7f seconds"%sumOfN2(100000))
  print("Sum is %d, it required %10.7f seconds"%sumOfN2(1000000))

print("Running benchmark tests for the sumofN3 method: ")

"""Running benchmark tests for values of n=10000,100000,1000000 using the sumOfN2 function"""
print("Sum is %d, it required %10.7f seconds"%sumofN3(10000))
print("Sum is %d, it required %10.7f seconds"%sumofN3(100000))
print("Sum is %d, it required %10.9f seconds"%sumofN3(1000000))
print("Sum is %d, it required %10.9f seconds"%sumofN3(10000000))
print("Sum is %d, it required %10.9f seconds"%sumofN3(100000000))
print("Sum is %d, it required %10.9f seconds"%sumofN3(1000000000))

