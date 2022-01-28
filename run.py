import os
os.chdir('source_code')

print("Hello there")

with open("sample.txt",'r') as f:
  for line in f.readlines():
    print(line)


print("file is closed")
