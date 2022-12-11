with open("01Input.txt") as f:
    data = f.read()
f.close()
maxi = 0
maxi2 = 0
maxi3 = 0
temp = 0
data = data.splitlines()
for lines in data:
    if lines == "":
        if temp > maxi:
            maxi = temp
        temp = 0
    else:
        temp += int(lines)
    
print(temp)

