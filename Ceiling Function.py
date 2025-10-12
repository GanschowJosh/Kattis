class Node:
  def __init__(self, val):
    self.val = val
    self.lchild = None
    self.rchild = None
  
class BST:
  def __init__(self, root=None):
    self.root = Node(root) if root else None

  def insert(self, val, currNode=None):
    if not currNode:
      currNode = self.root
    if val < currNode.val:
      if currNode.lchild == None:
        currNode.lchild = Node(val)
        return
      self.insert(val, currNode=currNode.lchild)
    elif val > currNode.val:
      if currNode.rchild == None:
        currNode.rchild = Node(val)
        return
      self.insert(val, currNode=currNode.rchild)
    else:
      return
  
  def serialize(self, currNode=None):
    if currNode == None:
      return "."
    else:
      return "("+self.serialize(currNode=currNode.lchild)+self.serialize(currNode=currNode.rchild)+")"
    


seen = set()
n, k = map(int, input().split())
for _ in range(n):
  curr = list(map(int, input().split()))
  currBST = BST(curr[0])
  for item in curr[1:]:
    currBST.insert(item)
  seen.add(currBST.serialize(currBST.root))
  # print(currBST.serialize(currBST.root))

print(len(seen))