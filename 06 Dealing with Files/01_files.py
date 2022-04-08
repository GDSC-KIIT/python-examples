# Reading a file

f = open("./zen.txt", 'r').readlines()

print(f)

for line in f:
  print(line)