print("Hello there")

with open("sample.txt",'w') as f:
  for line in f.readlines():
    print(line)


print("file is closed")
