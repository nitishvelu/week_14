"""
Write a program to find reciprocal of elements in given list,L=[‘a’,0,2] and handle the
exception when you are finding reciprocal for the values 0 and ‘a’.
"""
randomList = ['a', 0, 2]
for entry in randomList:
  try:
    print("The entry is", entry)
    r = 1/int(entry)
    break
  except:
    print("Next entry.")
    print()
print("The reciprocal of",entry,"is",r)
