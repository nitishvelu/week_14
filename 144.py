"""
Write a program to count the number of capital letters and small letters in a file. Write the
output to a separate file.
"""
fh=open("a.txt")
fx=open("b.txt","w")
count = 0
lcount = 0
text = fh.read()
for character in text:
  if character.isupper():
    count += 1
  elif character.islower():
    lcount+=1
print(count,lcount,file=fx)
