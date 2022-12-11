with open("04Input.txt") as f:
    data = f.read()
f.close()

data = data.splitlines()

out = 0

for item in data:
    first, second = item.split(",")
    beg1, end1 = map(int,first.split("-"))
    beg2, end2 = map(int,second.split("-"))
    if beg1 >= beg2 and end1 <= end2:
        out +=1
    elif beg1 <= beg2 and end1 >= end2:
        out +=1

print(out)
