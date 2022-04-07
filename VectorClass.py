class Vector:
  """Representation of vectors in a multidimensional space."""
  def __init__(self,d):
    self._coords = [0]*d  # create a vector of d dimensions.
  
  def __len__(self):
    return len(self._coords)

  def __getitem__(self,j):
    """Return the jth coordinate of a vector"""
    return self._coords[j]
  
  def __setitem__(self,j,value):
    """set the jth cooridnate of a vector"""
    self._coords[j] = value
  
  def __add__(self,other):
    """Returns the sum of the two vectors"""
    if(len(self)!=len(other)):
      raise ValueError("The dimensions of the two vectors must be equal!")
    resultant_vector = Vector(len(self))
    for i in range(len(self)):
      resultant_vector[i] = self[i]+ other[i]
    return resultant_vector
  
  def __eq__(self,other):
    """Check if two vectors are equal"""
    return self._coords==other._coords
  
  def __str__(self):
    """Return a string representation of a vector"""
    return "<" + str(self._coords)[1:-1]+ ">"


a = Vector(3)
b = Vector(3)
a[0],a[1],a[2] = 5,4,6
b[0],b[1],b[2] = 1,3,2
print(a+b)