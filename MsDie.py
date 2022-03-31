import random

class MsDie:
  def __init__(self,num_of_sides):
    self.num_of_sides = num_of_sides
    self.current_value = self.roll()
  
  def roll(self):
    self.current_value = random.randrange(1,self.num_of_sides+1)
    return self.current_value

  def __str__(self):
    return str(self.current_value)

  def __repr__(self):
    return f"MS Die({str(self.num_of_sides)}:{str(self.current_value)})"


my_die = MsDie(6)
for i in range(6):
  print(my_die,my_die.current_value)
  my_die.roll()

d_list = [MsDie(6),MsDie(20)]
print(d_list)