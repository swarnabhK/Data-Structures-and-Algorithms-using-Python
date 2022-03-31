
def gcds(m,n):
    while(m%n!=0):
      oldm = m
      oldn = n
      m = oldn
      n = oldm%oldn
    return n

class Fraction:
  def __init__(self,num,den) -> None: 
    if(not(isinstance(num, int) and isinstance(num, int))):
      raise ValueError("You need to use an integer!")
    else:
      gd = gcds(num,den)
      self.num = num//gd
      self.den = den//gd

  def getNum(self):
    return self.num

  def getDen(self):
    return self.den

  def __str__(self) -> str:
      return str(self.num)+"/"+str(self.den)
  
  def __add__(self,othernum):
    newnum= (self.num*othernum.den) + (othernum.num*self.den)
    newden = self.den*othernum.den
    return Fraction(newnum,newden)

  def __repr__(self):
    return str(self.num)+"/"+str(self.den)

  def __eq__(self,other):
    firstnum = self.num*other.den
    secondnum = other.num*self.den
    return firstnum == secondnum

    # implement *,/,-, >,<
  def __mul__(self,other):
    firstnum = self.num*other.num
    secondnum = self.den*other.den
    return Fraction(firstnum,secondnum)
  
  def __truediv__(self,other):
    firstnum = self.num*other.den
    secondnum = other.num*self.den
    return Fraction(firstnum,secondnum)

  def __sub__(self,othernum):
    newnum= (self.num*othernum.den) - (othernum.num*self.den)
    newden = self.den*othernum.den
    return Fraction(newnum,newden)
  
  def __gt__(self,other):
    firstnum = self.num*other.den
    secondnum = other.num*self.den

    return firstnum > secondnum

  def __ge__(self,other):
    firstnum = self.num*other.den
    secondnum = other.num*self.den

    return firstnum >= secondnum

  def __lt__(self,other):
    firstnum = self.num*other.den
    secondnum = other.num*self.den

    return firstnum < secondnum

  def __le__(self,other):
    firstnum = self.num*other.den
    secondnum = other.num*self.den

    return firstnum <= secondnum

  def __ne__(self,other):
    firstnum = self.num*other.den
    secondnum = other.num*self.den

    return firstnum != secondnum



f1 = Fraction(1,4)
f2 = Fraction(1,2)
f3 = f1+f2
f4 = Fraction(2,3)
f5 = Fraction(4,6)

print(f2+f4)
print(f2==f4)
print(f4==f5)
print(f4*f5)
print(f4/f5)
print(f1-f2)
f6 = Fraction(3,5)
f7 = Fraction(4,5)

print(f7!=f6)

print(Fraction(23.878,22))