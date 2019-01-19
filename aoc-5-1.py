def match(string1, string2):
  return string1.lower() == string2.lower() and string1 != string2

with open("aoc-5-1.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content][0]
checking = False

while True:
  i = 0
  while i < len(content) - 1:
    if match(content[i], content[i + 1]):
      checking = False
      content = content[:i] + content[i + 2:]
    else:
      i = i + 1
  if checking:
    break
  checking = True

print(len(content))
