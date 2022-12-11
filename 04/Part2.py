with open("04Input.txt") as f:
    data = f.read()
f.close()

data = data.splitlines()

out = 0

for item in data:
    first, second = item.split(",")
    beg1, end1 = map(int,first.split("-"))
    beg2, end2 = map(int,second.split("-"))
    if beg1 > beg2:
        if end2 >= beg1:
            out+=1
    elif beg1 < beg2:
        if end1 >=beg2:
            out+=1
    # Equal
    else:
        out+=1

print(out)