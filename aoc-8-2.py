class Node:

  def __init__(self, chil, meta):
    self.children = chil
    self.metadata = meta

def parseTree(currentString):
  metadata = []
  children = []

  childCount = int(currentString[0])
  metadataCount = int(currentString[1])
  currentString = currentString[2:]

  for i in range(childCount):
    child, currentString = parseTree(currentString)
    children.append(child)

  for i in range(metadataCount):
    metadata.append(int(currentString[i]))

  currentString = currentString[metadataCount:]

  return (Node(children, metadata), currentString)

def valuateNode(t):
  if len(t.children) == 0:
    s = 0
    for meta in t.metadata:
      s = s + meta
    return s
  else:
    s = 0
    for meta in t.metadata:
      if meta > len(t.children) or meta == 0:
        continue
      s = s + valuateNode(t.children[meta - 1])
    return s


with open("aoc-8-1.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content][0]

file = content.split(' ')


t,string = parseTree(file)

print(valuateNode(t))