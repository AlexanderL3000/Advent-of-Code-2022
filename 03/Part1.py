with open("03Input.txt") as f:
    data = f.read()
f.close()

data = data.splitlines()

total = 0
for item in data:
    first = set(item[:len(item)//2])
    second = set(item[len(item)//2:])
  
    for i in first:
        if i in second:
            if i.isupper():
                total += (ord(i)-38)
            else:
                total += (ord(i)-96)
print(total)