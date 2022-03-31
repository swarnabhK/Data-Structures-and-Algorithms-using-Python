import random


def generateString():
  random_string = ""
  l = list("abcdefghijklmn opqrstuvwxyz")
  for i in range(28):
    random_string+=random.choice(l)
  return random_string

def score_string(rs):
  g = "methinks it is like a weasel"
  score = 0
  for i in range(len(g)):
    if(g[i]==rs[i]):
      score=score+1
  return score/len(g)

def generate_score():
  rs = generateString()
  best = 0
  count = 0
  new_score = score_string(rs)
  while(new_score<1):
    if(new_score>best):
      print(new_score,rs)
      best = new_score
    count = count+1
    if(count%1000000==0):
      print(count,rs)
    rs = generateString()
    new_score = score_string(rs)

  return rs

print(generate_score())
