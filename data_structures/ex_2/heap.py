def heapsort(arr):
  new_heap = Heap()
  sorted_list = []
  for e in arr:
    new_heap.insert(e)
  while new_heap.size > 0:
    sorted_list.insert(0, new_heap.delete()) # insert this way has o(n) becoz it shifts every el to the back one spot
  return sorted_list                         # insert itself has o(log n)

  '''
  # Sean's solution which runtime is O(n log n)
  def heapsort(arr)
    heap = Heap()
    # initialize our sorted array to have length equal to our input array
    sorted = [0] * len(arr)
    for el in arr:
      heap.insert(el)
    for i in range(len(arr)):
      sorted[len(arr) - i - 1] = heap.delete() # `len(arr) - i - 1` = decendants loop
    return sorted
  '''

class Heap:
  def __init__(self):
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    self._bubble_up(self.size)

  def delete(self):
    retval = self.storage[1]
    self.storage[1] = self.storage[self.size]
    self.size -= 1
    self.storage.pop()
    self._sift_down(1)
    return retval 

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    while index // 2 > 0:
      if self.storage[index // 2] < self.storage[index]:
        self.storage[index], self.storage[index // 2] = self.storage[index // 2], self.storage[index]
      index = index // 2

  def _sift_down(self, index):
    while (index * 2) <= self.size:
      mc = self._max_child(index)
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      index = mc

  def _max_child(self, index):
    if index * 2 + 1 > self.size:
      return index * 2
    else:
      return index * 2 if self.storage[index * 2] > self.storage[index * 2 + 1] else index * 2 + 1