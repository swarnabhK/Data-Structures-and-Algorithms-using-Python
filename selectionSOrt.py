# start with first index, find minimum , swap with first, 
# increment index, find miniumum , swap with the incremented index

def SelectionSort(n):
  minium_index = 0
  for i in range(len(n)):
    minimum_index = n[i:].index(min(n[i:]))+i
    n[i],n[minimum_index] = n[minimum_index],n[i]
    print(n[i],n[minimum_index])
  return n


print(SelectionSort([9,2,45,69,103,-2,47,0]))