with open("03Input.txt") as f:
    data = f.read()
f.close()

data = data.splitlines()

total = 0
for i in range(0, len(data), 3):
    
    item = data[i]
    item2 = data[i+1]
    item3 = data[i+2]

    first = set(item)
    second = set(item2)
    third = set(item3)

    for j in first:
        if j in second and j in third:
            if j.isupper():
                total += (ord(j)-38)
            else:
                total += (ord(j)-96)
print(total)