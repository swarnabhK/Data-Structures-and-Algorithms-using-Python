"""A useless function to understand how time complexity is computed 
using Big-O notation"""

def useless_func(n):
  a=5
  b=6
  c=10
  for i in range(n):
    for j in range(n):
        x = i * i
        y = j * j
        z = i * j
  for k in range(n):
    w = a*k + 45
    v = b*b
  d = 33

# analyzing the performance(time complexity) of the above code snippet.
# T(n)=3+3n**2+2n+1
# 3 for the first three assignment statements.
# 3n**2 for the three assignments inside the nested loop iterations structure.
# 2n for the two assignment statements inside the for loop iteration.
# 1 for the assignment statement in the end.
# as n increases the n**2 term will become dominant, therefore for the above
# code snippet the time complexity is O(n**2)

