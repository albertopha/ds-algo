class TreeNode():
 def __init__(self, text=''):
  self.text = text
  self.isWord = False
  self.children = dict()

 def get_text(self):
  return self.text

 def set_text(self, text):
  self.text = text

 def is_word(self):
  return self.isWord

 def set_is_word(self, isWord):
  self.isWord = isWord

 def get_children(self):
  return self.children

 def set_children(self, children):
  self.children = children


class Trie():
 def __init__(self):
  self.root = TreeNode()

 def insert(self, text):
  current = self.root
  for i, c in enumerate(text):
   children = current.get_children()
   if c not in children:
    children[c] = TreeNode(c)  
   current = children[c]
  current.set_is_word(True)
  
 def search(self, target):
  current = self.root
  for i, c in enumerate(target):
   if not current:
     return False

   children = current.get_children()
   if c not in children:
    return False

   current = children[c]

  return current.is_word()

 def __str__(self):
  def printTree(root):
   if not root:
    return

   print(root.text)
   for i, node in enumerate(root.children.values()):
    printTree(node)

  printTree(self.root)
  return ''

if __name__ == '__main__':
 trie = Trie()
 trie.insert("hello")
 trie.insert("world")
 trie.insert("search")
 print(trie)
 print(trie.search("hello"))
 print(trie.search("helloword"))
