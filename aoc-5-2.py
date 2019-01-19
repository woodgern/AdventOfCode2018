def match(string1, string2):
  return string1.lower() == string2.lower() and string1 != string2

def collapseString(string):
  checking = False

  while True:
    i = 0
    while i < len(string) - 1:
      if match(string[i], string[i + 1]):
        checking = False
        string = string[:i] + string[i + 2:]
      else:
        i = i + 1
    if checking:
      break
    checking = True

  return string


with open("aoc-5-1.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content][0]

shortest = 50000
for A in range(65, 65 + 26):
  print("Checking {}".format(chr(A)))
  content_A = content.replace(chr(A), "").replace(chr(A).lower(), "")
  length = len(collapseString(content_A))

  if length < shortest:
    shortest = length

print(shortest)
