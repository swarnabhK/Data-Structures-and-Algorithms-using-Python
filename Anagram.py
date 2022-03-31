
def AnagramSolution1(s1,s2):
  """for each element in the outerlist:
a) check if the element is present in the inner list.
b) keep iterating in the inner list until the item is not found.
c) If the item is found in the innerlist, replace the item with 
None.
if the outerlist item is not found in the innerlist, then return false. Time complexity is O(n**2)."""

  keepRunning = True
  if(len(s1)!=len(s2)):
    keepRunning = False

  s2_list = list(s2)
  pos1 = 0
  
  while(pos1<len(s1) and keepRunning):
    pos2 = 0
    found = False
    while(pos2<len(s2_list) and not found):
      if(s1[pos1]==s2_list[pos2]):
        found= True
      else:
        pos2+=1
    if found:
      s2_list[pos2] = None
    else:
      keepRunning = False
    pos1 = pos1+1
  return keepRunning

def AnagramSolution2(s1,s2):
  """Sort the two string lists and compare each element for both the lists. If each element is equal then the strings are anagrams. Time Complezity is O(n**2). Not a better solution than the above solution."""

  if(len(s1)!=len(s2)):
    return False
  s1_list = list(s1)
  s2_list = list(s2)
  s1_list.sort()
  s2_list.sort()
  for i in range(len(s1_list)):
    if(s1_list[i]!=s2_list[i]):
      return False
  return True

def AnagramSolution3(s1,s2):
  """Creating two dictionaries to keep counts of the letter frequencies of the two strings. If the frequencies are equal, the two strings are anagrams."""

  if(len(s1)!=len(s2)):
    return False
  new_key = list("abcdefghijklmnopqrstuvwxyz")
  dict_s1 = dict.fromkeys(new_key, 0)
  dict_s2 = dict.fromkeys(new_key, 0)
  for i in s1:
    if i in dict_s1:
      dict_s1[i]+=1
  for i in s2:
    if i in dict_s2:
      dict_s2[i]+=1
  for i in s1:
    if(dict_s1[i]!=dict_s2[i]):
      return False
  return True


print("Testing the AnagramSolution1 method: ")
print()
print(AnagramSolution1('abcd','dcba'))
print(AnagramSolution1('python','typhon'))
print()
print("Testing the AnagramSolution2 method: ")
print()
print(AnagramSolution2('abcd','dcba'))
print(AnagramSolution2('python','typhon'))
print(AnagramSolution2('abey','kela'))
print()
print("Testing the AnagramSolution3 method: ")
print()
print(AnagramSolution3('abcd','dcba'))
print(AnagramSolution3('python','typhon'))
print(AnagramSolution3('abey','kela'))