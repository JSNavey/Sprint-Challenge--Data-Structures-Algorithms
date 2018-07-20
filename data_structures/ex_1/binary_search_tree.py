from collections import deque

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    # recursive
    # call the cb on the current BST node
    # always check on the left first
    cb(self.value)
    if self.left is not None: # can be `if self.left` as well
      self.left.depth_first_for_each(cb)
    if self.right is not None:
      self.right.depth_first_for_each(cb)
    return

    '''
    # iterative - Sean's solution
    stack = []
    stack.append(self)
    while len(stack):
      current_node = stack.pop()
      if current_node.right:  # if start with left, the order of number will be flipped as the search will go right instead.
        stack.append(current_node.right)
      if current_node.left:
        stack.append(current_node.left)
      cb(current_node.value)
    '''

  def breadth_first_for_each(self, cb):
    # FIFO order
    queue = []
    queue.append(self)
    while len(queue) > 0:  # can be `while len(queue)`
      curr_node = queue.pop(0)
      if curr_node.left is not None:
        queue.append(curr_node.left)  # can switch from right to left but the order of list will change too.
      if curr_node.right is not None: 
        queue.append(curr_node.right)
      cb(curr_node.value)
      

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
