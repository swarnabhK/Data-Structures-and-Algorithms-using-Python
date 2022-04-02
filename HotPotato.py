class Queue:
  def __init__(self):

    self.items = []

  def isEmpty(self):
    return self.items == []

  def enqueue(self,item):
    self.items.insert(0,item)
  
  def dequeue(self):
    return self.items.pop()
  
  def queue_size(self):
    return len(self.items)


def hotPotato(namelist, num):

  """Method to simulate the hotpotato game, In this game children line up in a circle and pass an item from neighbor to neighbor as fast as they can. At a certain point in the game, the action is stopped and the child who has the item (the potato) is removed from the circle. Play continues until only one child is left.
"""

  q = Queue()
  for name in namelist:
    q.enqueue(name)
    
  while(q.queue_size()>1):
    for i in range(num):
      q.enqueue(q.dequeue())
    q.dequeue()

  return q.dequeue()


print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
