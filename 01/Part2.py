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
            maxi3 = maxi2
            maxi2 = maxi
            maxi = temp
        elif temp>maxi2:
            maxi3 = maxi2
            maxi2 = temp
        elif temp> maxi3:
            maxi3 =temp
        temp = 0
    else:
        temp += int(lines)
    
print(maxi+maxi2+maxi3)