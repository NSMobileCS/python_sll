from collections import deque as Dq
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class SLL(object):
  def __init__(self, arr=None):
    if arr:
      node = ListNode(arr.pop(0))
      self.head = node
      while arr:
        lastnode, node = node, ListNode(arr.pop(0))
        lastnode.next = node
    else:
      self.head = None

  def to_array(self):
    arr = Dq()
    cur = self.head
    while cur:
      arr.append(cur.val)
      cur = cur.next
    return arr

  def __str__(self):
    return repr(self)

  def __repr__(self):
    return "<[SLLHead]>-->([" + "])-->([".join([str(x) for x in self.to_array()]) + "])--><[None]>"


