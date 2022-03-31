

def minimum1(l):
  """This function compares each number to every other number on the list.
  O(n**2) time complexity"""

  minimum = l[0]
  for i in range(len(l)):
    isSmallest = True
    for j in range(len(l)):
      if(l[i]>l[j]):
        isSmallest = False
    if(isSmallest):
      minimum = l[i]
  return minimum

def minimum2(l):
  """This function has linear O(n) time complexity"""
  minimum = l[0]
  for i in range(len(l)):
    if(l[i]<minimum):
      minimum = l[i]
  return minimum

print(minimum1([-108,4,-56,90,23]))
print(minimum2([-108,4,-56,90,23]))
