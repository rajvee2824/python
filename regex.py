import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")



txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
x = re.findall("Portugal", txt)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

x = re.split("\s", txt)
print(x)
  
x = re.split("\s", txt, 1)
print(x)
x = re.sub("\s", "9", txt)
print(x)
x = re.sub("\s", "9", txt, 2)
print(x)

x = re.search("ai", txt)
print(x) #this will print an object

x = re.search(r"\bS\w+", txt)
print(x.span())

x = re.search(r"\bS\w+", txt)
print(x.string)



x = re.search(r"\bS\w+", txt)
print(x.group())